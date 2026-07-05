from sqlalchemy.orm import Session

from app.models.sale import Sale


class SaleRepository:

    def create(
        self,
        db: Session,
        sale: Sale,
    ):
        db.add(sale)
        return sale

    def get_all(self, db: Session):
        return db.query(Sale).all()

    def get_by_id(
        self,
        db: Session,
        sale_id: int,
    ):
        return (
            db.query(Sale)
            .filter(Sale.id == sale_id)
            .first()
        )


sale_repository = SaleRepository()