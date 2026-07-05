from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.purchase import (
    PurchaseCreate,
    PurchaseResponse,
)
from app.services.purchase import purchase_service

router = APIRouter(
    prefix="/purchases",
    tags=["Purchases"],
)


@router.post(
    "",
    response_model=PurchaseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_purchase(
    purchase: PurchaseCreate,
    db: Session = Depends(get_db),
):
    return purchase_service.create_purchase(
        db,
        purchase,
    )


@router.get(
    "",
    response_model=list[PurchaseResponse],
)
def get_all_purchases(
    db: Session = Depends(get_db),
):
    return purchase_service.get_all_purchases(db)


@router.get(
    "/{purchase_id}",
    response_model=PurchaseResponse,
)
def get_purchase(
    purchase_id: int,
    db: Session = Depends(get_db),
):
    return purchase_service.get_purchase_by_id(
        db,
        purchase_id,
    )


@router.delete("/{purchase_id}")
def delete_purchase(
    purchase_id: int,
    db: Session = Depends(get_db),
):
    return purchase_service.delete_purchase(
        db,
        purchase_id,
    )