from sqlalchemy.orm import Session

from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate, SupplierUpdate


class SupplierRepository:

    def create(
        self,
        db: Session,
        supplier: SupplierCreate,
    ) -> Supplier:

        db_supplier = Supplier(
            name=supplier.name,
            email=supplier.email,
            phone=supplier.phone,
            address=supplier.address,
        )

        db.add(db_supplier)
        db.commit()
        db.refresh(db_supplier)

        return db_supplier

    def get_by_id(
        self,
        db: Session,
        supplier_id: int,
    ):
        return (
            db.query(Supplier)
            .filter(Supplier.id == supplier_id)
            .first()
        )

    def get_by_name(
        self,
        db: Session,
        name: str,
    ):
        return (
            db.query(Supplier)
            .filter(Supplier.name == name)
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str,
    ):
        return (
            db.query(Supplier)
            .filter(Supplier.email == email)
            .first()
        )

    def get_by_phone(
        self,
        db: Session,
        phone: str,
    ):
        return (
            db.query(Supplier)
            .filter(Supplier.phone == phone)
            .first()
        )

    def get_all(self, db: Session):
        return (
            db.query(Supplier)
            .order_by(Supplier.id)
            .all()
        )

    def update(
        self,
        db: Session,
        db_supplier: Supplier,
        supplier: SupplierUpdate,
    ):
        update_data = supplier.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_supplier, key, value)

        db.commit()
        db.refresh(db_supplier)

        return db_supplier

    def delete(
        self,
        db: Session,
        db_supplier: Supplier,
    ):
        db.delete(db_supplier)
        db.commit()


supplier_repository = SupplierRepository()