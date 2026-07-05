from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_categories: int
    total_products: int
    total_suppliers: int
    total_purchases: int
    total_sales: int


class LowStockProduct(BaseModel):
    id: int
    name: str
    stock_quantity: int


class OutOfStockProduct(BaseModel):
    id: int
    name: str


class RecentPurchase(BaseModel):
    id: int
    product_name: str
    supplier_name: str
    quantity: int


class RecentSale(BaseModel):
    id: int
    product_name: str
    quantity: int
    total_amount: float