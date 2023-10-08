from pydantic import BaseModel, constr, conint, Field, UUID4
from uuid import uuid4
class UpdateModel(BaseModel):
    class Config:
        extra = "forbid"

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