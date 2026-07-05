from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class PurchaseCreate(BaseModel):
    supplier_id: int
    product_id: int
    quantity: int = Field(..., gt=0)
    unit_price: float = Field(..., gt=0)


class PurchaseUpdate(BaseModel):
    quantity: int | None = Field(default=None, gt=0)
    unit_price: float | None = Field(default=None, gt=0)


class PurchaseResponse(BaseModel):
    id: int
    supplier_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_amount: float
    purchase_date: datetime

    model_config = ConfigDict(from_attributes=True)