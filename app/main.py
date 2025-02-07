from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import routes_places
from app.models.model_places import Base
from app.database import engine

Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(routes_places.router, prefix="/places", tags=["places"])
