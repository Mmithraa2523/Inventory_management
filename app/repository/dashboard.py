from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.product import Product
from app.models.purchase import Purchase
from app.models.sale import Sale
from app.models.supplier import Supplier


class DashboardRepository:

    def get_summary(self, db: Session):
        return {
            "total_categories": db.query(func.count(Category.id)).scalar(),
            "total_products": db.query(func.count(Product.id)).scalar(),
            "total_suppliers": db.query(func.count(Supplier.id)).scalar(),
            "total_purchases": db.query(func.count(Purchase.id)).scalar(),
            "total_sales": db.query(func.count(Sale.id)).scalar(),
        }

    def get_low_stock_products(self, db: Session):
        return (
            db.query(Product)
            .filter(Product.stock_quantity <= 5)
            .order_by(Product.stock_quantity.asc())
            .all()
        )

    def get_out_of_stock_products(self, db: Session):
        return (
            db.query(Product)
            .filter(Product.stock_quantity == 0)
            .all()
        )

    def get_recent_purchases(self, db: Session):
        return (
            db.query(Purchase)
            .order_by(Purchase.purchase_date.desc())
            .limit(5)
            .all()
        )

    def get_recent_sales(self, db: Session):
        return (
            db.query(Sale)
            .order_by(Sale.sale_date.desc())
            .limit(5)
            .all()
        )


dashboard_repository = DashboardRepository()