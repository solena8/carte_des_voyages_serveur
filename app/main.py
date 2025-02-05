from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.api.routes import places
from app.dependencies import get_db
from app.models.places import Base
from app.database import engine
from app.models.places import Place

# Créer les tables dans la base de données
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # URL de votre frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def read_places(db: Session = Depends(get_db)):
    places = db.query(Place).all()
    return JSONResponse(content=[{
        "name": place.name,
        "date": place.date.isoformat(),
        "city": place.city,
        "country": place.country,
        "latitude": place.latitude,
        "longitude": place.longitude,
        "image": place.image.decode('utf-8') if place.image else None
    } for place in places])
app.include_router(places.router, prefix="/places", tags=["places"])
