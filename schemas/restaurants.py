from typing import Optional
from pydantic import BaseModel, constr, conint, Field, UUID4
from uuid import uuid4
class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

# class ErrorResponse(BaseModel):
#     message: str

class RestaurantRequest(UpdateModel):
    rating: conint(ge=0, le=4)
    name: str
    site: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    lat: float
    ing: float

class RestaurantResponse(UpdateModel):
    id: UUID4
    rating: conint(ge=0, le=4)
    name: str
    site: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    lat: float
    ing: float

class UpdateRestaurantRequest(UpdateModel):
    rating: Optional[conint(ge=0, le=4)]
    name: Optional[str] 
    site: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    lat: Optional[float]
    ing: Optional[float]