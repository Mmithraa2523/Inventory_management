from sqlalchemy.orm import Session

from app.repository.dashboard import dashboard_repository


class DashboardService:

    def get_summary(self, db: Session):
        return dashboard_repository.get_summary(db)

    def get_low_stock_products(self, db: Session):
        return dashboard_repository.get_low_stock_products(db)

    def get_out_of_stock_products(self, db: Session):
        return dashboard_repository.get_out_of_stock_products(db)

    def get_recent_purchases(self, db: Session):
        return dashboard_repository.get_recent_purchases(db)

    def get_recent_sales(self, db: Session):
        return dashboard_repository.get_recent_sales(db)


dashboard_service = DashboardService()