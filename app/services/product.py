from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.category import category_repository
from app.repository.product import product_repository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:

    def create_product(self, db: Session, product: ProductCreate):

        if product_repository.get_by_name(db, product.name):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product already exists",
            )

        if not category_repository.get_by_id(db, product.category_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )

        return product_repository.create(db, product)

    def get_all_products(self, db: Session):
        return product_repository.get_all(db)

    def get_product_by_id(self, db: Session, product_id: int):
        product = product_repository.get_by_id(db, product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        return product

    def update_product(
        self,
        db: Session,
        product_id: int,
        product: ProductUpdate,
    ):
        db_product = self.get_product_by_id(db, product_id)

        return product_repository.update(db, db_product, product)

    def delete_product(self, db: Session, product_id: int):
        db_product = self.get_product_by_id(db, product_id)

        product_repository.delete(db, db_product)

        return {"message": "Product deleted successfully"}


product_service = ProductService()