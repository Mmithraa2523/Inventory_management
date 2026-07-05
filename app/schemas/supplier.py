from pydantic import BaseModel, ConfigDict, EmailStr, Field


class SupplierCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    address: str | None = Field(default=None, max_length=255)


class SupplierUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=10, max_length=15)
    address: str | None = Field(default=None, max_length=255)


class SupplierResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str | None

    model_config = ConfigDict(from_attributes=True)