from fastapi import FastAPI
from app.database.connection import Base,engine
import app.models
from app.routers.category import router as category_router
from app.routers.product import router as product_router
from app.routers.supplier import router as supplier_router
from app.routers.purchase import router as purchase_router
from app.routers.dashboard import router as dashboard_router
app = FastAPI()
@app.get("/")
def root():
    return {"message": "Inventory management API"}

@app.get("/about")
def about():
    return {
        "project":"Inventory management API",
        "developer":"Mithraa",
        "version":"1.0.0"
    }

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(category_router)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(purchase_router)
app.include_router(dashboard_router)