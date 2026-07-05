from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


class CategoryRepository:

    def create(self, db: Session, category: CategoryCreate) -> Category:
        db_category = Category(
            name=category.name,
            description=category.description,
        )

        db.add(db_category)
        db.commit()
        db.refresh(db_category)

        return db_category

    def get_by_id(self, db: Session, category_id: int):
        return db.query(Category).filter(
            Category.id == category_id
        ).first()

    def get_by_name(self, db: Session, name: str):
        return db.query(Category).filter(
            Category.name == name
        ).first()

    def get_all(self, db: Session):
        return db.query(Category).order_by(
            Category.id
        ).all()

    def update(
        self,
        db: Session,
        db_category: Category,
        category: CategoryUpdate,
    ):
        update_data = category.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_category, key, value)

        db.commit()
        db.refresh(db_category)

        return db_category

    def delete(self, db: Session, db_category: Category):
        db.delete(db_category)
        db.commit()


category_repository = CategoryRepository()