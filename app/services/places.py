from sqlalchemy.orm import Session
from app.models.places import Place
from app.schemas.places import PlaceCreate

def create_new_place(db: Session, place: PlaceCreate):
    db_place = Place(
        name=place.name,
        date=place.date,
        city=place.city,
        country=place.country,
        latitude=place.latitude,
        longitude=place.longitude,
        image=place.image
    )
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place
