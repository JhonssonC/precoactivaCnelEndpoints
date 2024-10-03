from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, create_db_and_tables
from .crud import get_nearest_sequence
from pydantic import BaseModel

app = FastAPI()

class Coordinate(BaseModel):
    x: float
    y: float

@app.on_event("startup")
def startup():
    create_db_and_tables()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/route/")
def get_route(coordinate: Coordinate, db: Session = Depends(get_db)):
    result = get_nearest_sequence(db, coordinate.x, coordinate.y)
    if not result:
        raise HTTPException(status_code=404, detail="Sequence not found")
    return result

