from sqlalchemy.orm import Session

from app.models.purchase import Purchase
from app.schemas.purchase import PurchaseCreate, PurchaseUpdate


class PurchaseRepository:

    def create(
        self,
        db: Session,
        purchase: PurchaseCreate,
        total_amount: float,
    ):
        db_purchase = Purchase(
            supplier_id=purchase.supplier_id,
            product_id=purchase.product_id,
            quantity=purchase.quantity,
            unit_price=purchase.unit_price,
            total_amount=total_amount,
        )

        db.add(db_purchase)

        return db_purchase

    def get_all(self, db: Session):
        return db.query(Purchase).all()

    def get_by_id(
        self,
        db: Session,
        purchase_id: int,
    ):
        return (
            db.query(Purchase)
            .filter(Purchase.id == purchase_id)
            .first()
        )

    def delete(
        self,
        db: Session,
        purchase: Purchase,
    ):
        db.delete(purchase)


purchase_repository = PurchaseRepository()