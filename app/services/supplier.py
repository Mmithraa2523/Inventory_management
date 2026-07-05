from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.supplier import supplier_repository
from app.schemas.supplier import SupplierCreate, SupplierUpdate


class SupplierService:

    def create_supplier(
        self,
        db: Session,
        supplier: SupplierCreate,
    ):

        if supplier_repository.get_by_name(db, supplier.name):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Supplier name already exists",
            )

        if supplier_repository.get_by_email(db, supplier.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists",
            )

        if supplier_repository.get_by_phone(db, supplier.phone):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone number already exists",
            )

        return supplier_repository.create(db, supplier)

    def get_all_suppliers(self, db: Session):
        return supplier_repository.get_all(db)

    def get_supplier_by_id(
        self,
        db: Session,
        supplier_id: int,
    ):
        supplier = supplier_repository.get_by_id(
            db,
            supplier_id,
        )

        if not supplier:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Supplier not found",
            )

        return supplier

    def update_supplier(
        self,
        db: Session,
        supplier_id: int,
        supplier: SupplierUpdate,
    ):
        db_supplier = self.get_supplier_by_id(
            db,
            supplier_id,
        )

        # Check duplicate name
        if (
            supplier.name
            and supplier.name != db_supplier.name
            and supplier_repository.get_by_name(db, supplier.name)
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Supplier name already exists",
            )

        # Check duplicate email
        if (
            supplier.email
            and supplier.email != db_supplier.email
            and supplier_repository.get_by_email(db, supplier.email)
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists",
            )

        # Check duplicate phone
        if (
            supplier.phone
            and supplier.phone != db_supplier.phone
            and supplier_repository.get_by_phone(db, supplier.phone)
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone number already exists",
            )

        return supplier_repository.update(
            db,
            db_supplier,
            supplier,
        )

    def delete_supplier(
        self,
        db: Session,
        supplier_id: int,
    ):
        db_supplier = self.get_supplier_by_id(
            db,
            supplier_id,
        )

        supplier_repository.delete(
            db,
            db_supplier,
        )

        return {
            "message": "Supplier deleted successfully"
        }


supplier_service = SupplierService()