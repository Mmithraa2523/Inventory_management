from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.dashboard import (
    DashboardSummary,
    LowStockProduct,
    OutOfStockProduct,
    RecentPurchase,
    RecentSale,
)
from app.services.dashboard import dashboard_service

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/summary",
    response_model=DashboardSummary,
)
def get_summary(
    db: Session = Depends(get_db),
):
    return dashboard_service.get_summary(db)


@router.get(
    "/low-stock",
    response_model=list[LowStockProduct],
)
def get_low_stock_products(
    db: Session = Depends(get_db),
):
    return dashboard_service.get_low_stock_products(db)


@router.get(
    "/out-of-stock",
    response_model=list[OutOfStockProduct],
)
def get_out_of_stock_products(
    db: Session = Depends(get_db),
):
    return dashboard_service.get_out_of_stock_products(db)


@router.get(
    "/recent-purchases",
    response_model=list[RecentPurchase],
)
def get_recent_purchases(
    db: Session = Depends(get_db),
):
    purchases = dashboard_service.get_recent_purchases(db)

    return [
        {
            "id": purchase.id,
            "product_name": purchase.product.name,
            "supplier_name": purchase.supplier.name,
            "quantity": purchase.quantity,
        }
        for purchase in purchases
    ]


@router.get(
    "/recent-sales",
    response_model=list[RecentSale],
)
def get_recent_sales(
    db: Session = Depends(get_db),
):
    sales = dashboard_service.get_recent_sales(db)

    return [
        {
            "id": sale.id,
            "product_name": sale.product.name,
            "quantity": sale.quantity,
            "total_amount": float(sale.total_amount),
        }
        for sale in sales
    ]