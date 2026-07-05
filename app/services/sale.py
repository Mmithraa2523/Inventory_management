from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.repository.product import product_repository
from app.repository.sale import sale_repository
from app.schemas.sale import SaleCreate


class SaleService:

    def create_sale(
        self,
        db: Session,
        sale: SaleCreate,
    ):

        product = product_repository.get_by_id(
            db,
            sale.product_id,
        )

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        if product.stock_quantity < sale.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient stock",
            )

        total_amount = sale.quantity * float(product.price)

        db_sale = Sale(
            product_id=sale.product_id,
            quantity=sale.quantity,
            unit_price=product.price,
            total_amount=total_amount,
        )

        sale_repository.create(db, db_sale)

        product.stock_quantity -= sale.quantity

        db.commit()
        db.refresh(db_sale)

        return db_sale

    def get_all_sales(self, db: Session):
        return sale_repository.get_all(db)


sale_service = SaleService()