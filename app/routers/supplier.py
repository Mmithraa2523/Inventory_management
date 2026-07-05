from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.supplier import (
    SupplierCreate,
    SupplierResponse,
    SupplierUpdate,
)
from app.services.supplier import supplier_service

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"],
)


@router.post(
    "",
    response_model=SupplierResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db),
):
    return supplier_service.create_supplier(db, supplier)


@router.get(
    "",
    response_model=list[SupplierResponse],
)
def get_all_suppliers(
    db: Session = Depends(get_db),
):
    return supplier_service.get_all_suppliers(db)


@router.get(
    "/{supplier_id}",
    response_model=SupplierResponse,
)
def get_supplier(
    supplier_id: int,
    db: Session = Depends(get_db),
):
    return supplier_service.get_supplier_by_id(
        db,
        supplier_id,
    )


@router.put(
    "/{supplier_id}",
    response_model=SupplierResponse,
)
def update_supplier(
    supplier_id: int,
    supplier: SupplierUpdate,
    db: Session = Depends(get_db),
):
    return supplier_service.update_supplier(
        db,
        supplier_id,
        supplier,
    )


@router.delete(
    "/{supplier_id}",
    status_code=status.HTTP_200_OK,
)
def delete_supplier(
    supplier_id: int,
    db: Session = Depends(get_db),
):
    return supplier_service.delete_supplier(
        db,
        supplier_id,
    )