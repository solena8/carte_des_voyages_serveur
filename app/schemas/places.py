from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Config:
    from_attributes = True


class Place(BaseModel):
    id: int = None
    name: str
    date: datetime = None
    city: str
    country: str
    latitude: float
    longitude: float
    image: Optional[bytes] = None


class PlaceCreate(BaseModel):
    name: str
    date: datetime
    city: str
    country: str
    latitude: float
    longitude: float
    image: Optional[bytes] = None

