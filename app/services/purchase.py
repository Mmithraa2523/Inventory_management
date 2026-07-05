from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.product import Product
from app.repository.product import product_repository
from app.repository.purchase import purchase_repository
from app.repository.supplier import supplier_repository
from app.schemas.purchase import PurchaseCreate


class PurchaseService:

    def create_purchase(
        self,
        db: Session,
        purchase: PurchaseCreate,
    ):

        supplier = supplier_repository.get_by_id(
            db,
            purchase.supplier_id,
        )

        if not supplier:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Supplier not found",
            )

        product = product_repository.get_by_id(
            db,
            purchase.product_id,
        )

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        total_amount = (
            purchase.quantity * purchase.unit_price
        )

        db_purchase = purchase_repository.create(
            db,
            purchase,
            total_amount,
        )

        product.stock_quantity += purchase.quantity

        db.commit()

        db.refresh(db_purchase)

        return db_purchase

    def get_all_purchases(self, db: Session):
        return purchase_repository.get_all(db)

    def get_purchase_by_id(
        self,
        db: Session,
        purchase_id: int,
    ):
        purchase = purchase_repository.get_by_id(
            db,
            purchase_id,
        )

        if not purchase:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Purchase not found",
            )

        return purchase

    def delete_purchase(
        self,
        db: Session,
        purchase_id: int,
    ):
        purchase = self.get_purchase_by_id(
            db,
            purchase_id,
        )

        purchase_repository.delete(
            db,
            purchase,
        )

        db.commit()

        return {
            "message": "Purchase deleted successfully"
        }


purchase_service = PurchaseService()