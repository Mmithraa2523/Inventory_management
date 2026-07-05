from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.category import category_repository
from app.schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:

    def create_category(self, db: Session, category: CategoryCreate):
        existing_category = category_repository.get_by_name(
            db,
            category.name
        )

        if existing_category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category already exists"
            )

        return category_repository.create(db, category)

    def get_all_categories(self, db: Session):
        return category_repository.get_all(db)

    def get_category_by_id(self, db: Session, category_id: int):
        category = category_repository.get_by_id(db, category_id)

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )

        return category

    def update_category(
        self,
        db: Session,
        category_id: int,
        category: CategoryUpdate
    ):
        db_category = self.get_category_by_id(db, category_id)

        return category_repository.update(
            db,
            db_category,
            category
        )

    def delete_category(self, db: Session, category_id: int):
        db_category = self.get_category_by_id(db, category_id)

        category_repository.delete(db, db_category)

        return {
            "message": "Category deleted successfully"
        }


category_service = CategoryService()