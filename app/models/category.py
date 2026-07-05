from sqlalchemy import String,DateTime
from datetime import datetime,UTC
from sqlalchemy.orm import Mapped, mapped_column
from app.database.connection import Base
from sqlalchemy.orm import relationship
class Category(Base):
    __tablename__="categories"
    id:Mapped[int] = mapped_column(primary_key=True,index=True)
    name:Mapped[str] = mapped_column(String(100),unique=True,nullable=False)
    description:Mapped[str|None] = mapped_column(String(255),nullable=True)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now(UTC))
    updated_at:Mapped[datetime] = mapped_column(
        DateTime,default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
        
    )
    products = relationship(
    "Product",
    back_populates="category",
    cascade="all, delete-orphan"
)