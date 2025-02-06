from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.places import create_new_place
from app.schemas import places as schemas
from app.dependencies import get_db
from app.models.places import Place
from starlette.responses import JSONResponse
from fastapi import Depends, status, HTTPException

router = APIRouter()

@router.post("/", response_model=schemas.PlaceCreate)
def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    return create_new_place(db=db, place=place)

@router.get("/")
async def read_places(db: Session = Depends(get_db)):
    places = db.query(Place).all()
    return JSONResponse(content=[{
        "id": place.id,
        "name": place.name,
        "date": place.date.isoformat(),
        "city": place.city,
        "country": place.country,
        "latitude": place.latitude,
        "longitude": place.longitude,
        "image": place.image.decode('utf-8') if place.image else None
    } for place in places])


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_place(id: int, db: Session = Depends(get_db)):
    place = db.query(Place).filter(Place.id == id).first()
    if place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    db.delete(place)
    db.commit()
    return {"message": "Place deleted successfully"}
