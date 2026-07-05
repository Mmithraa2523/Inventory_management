from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SaleCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class SaleResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float
    total_amount: float
    sale_date: datetime

    model_config = ConfigDict(from_attributes=True)