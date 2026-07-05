from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.schemas.category import(
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
from app.services.category import category_service

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)
@router.post(
    "",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    return category_service.create_category(db, category)

@router.get(
    "",
    response_model=list[CategoryResponse],
)
def get_all_categories(
    db: Session = Depends(get_db),
):
    return category_service.get_all_categories(db)

@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    return category_service.get_category_by_id(
        db,
        category_id,
    )

@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
):
    return category_service.update_category(
        db,
        category_id,
        category,
    )
@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    return category_service.delete_category(
        db,
        category_id,
    )
