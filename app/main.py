from fastapi import FastAPI
from app.database.connection import Base,engine
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


