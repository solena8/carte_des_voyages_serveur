from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.places import create_new_place
from app.schemas import places as schemas
from app.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=schemas.PlaceCreate)
def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    return create_new_place(db=db, place=place)
