from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.connection import Base
class Category(Base):
    __tablename__="categories"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(100),unique=True,nullable=False)
    description:Mapped[str|None] = mapped_column(String(255),nullable=True)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)
    updated_at:Mapped[datetime] = mapped_column(
        DateTime,default=datetime.utcnow,
        onupdate=datetime.utcnow
    )