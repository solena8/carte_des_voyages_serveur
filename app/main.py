from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import places
from app.models.places import Base
from app.database import engine

Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(places.router, prefix="/places", tags=["places"])
