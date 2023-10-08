from fastapi import APIRouter, Depends, Request
from schemas.restaurants import RestaurantRequest, RestaurantResponse
from configs.database import get_db
from services.restaurants import RestautantService
router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
)

@router.get("/", response_model=list[RestaurantResponse])
async def get_all_restaurants(db: get_db = Depends()):
    restaurants = RestautantService(db).get_all()
    for restaurant in restaurants:
        restaurant.__dict__.pop("_sa_instance_state")
    return restaurants

@router.post("/", status_code=201, response_model=RestaurantResponse)
async def create_restaurant(item: RestaurantRequest, db: get_db = Depends()):
    item = item.__dict__
    restaurant = RestautantService(db).create(item)
    return restaurant

@router.get("/{restaurant_id}")
async def get_restaurant(restaurant_id: str):
    return {"message": f"Get restaurant with id {restaurant_id}"}

@router.patch("/{restaurant_id}")
async def update_restaurant(restaurant_id: str):
    return {"message": f"Update restaurant with id {restaurant_id}"}