from typing import Optional
from pydantic import BaseModel, constr, conint, Field, UUID4
from uuid import uuid4
class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

class RestaurantRequest(UpdateModel):
    rating: conint(ge=0, le=4)
    name: str
    site: str
    email: str = Field(max_length=50,pattern=r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
    phone: str
    street: str
    city: str
    state: str
    lat: float
    lng: float

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
    lng: float

class UpdateRestaurantRequest(BaseModel):
    rating: Optional[conint(ge=0, le=4)]
    name: Optional[str] = None
    site: Optional[str]= None
    email: Optional[str] = Field(
    None,
    pattern=r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$",
    max_length=50)
    phone: Optional[str]= None
    street: Optional[str]= None
    city: Optional[str]= None
    state: Optional[str]= None
    lat: Optional[float]= None
    lng: Optional[float]= None