from fastapi import APIRouter, Depends, HTTPException, Request
from schemas.restaurants import RestaurantRequest, RestaurantResponse
from configs.database import get_db
from services.restaurants import RestaurantService
from uuid import UUID

router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
)


@router.get("/", response_model=list[RestaurantResponse])
async def get_all_restaurants(db: get_db = Depends()):
    restaurants = RestaurantService(db).get_all()
    for restaurant in restaurants:
        restaurant.__dict__.pop("_sa_instance_state")
    return restaurants

@router.post("/", status_code=201, response_model=RestaurantResponse)
async def create_restaurant(item: RestaurantRequest, db: get_db = Depends()):
    item = item.__dict__
    restaurant = RestaurantService(db).create(item)
    return restaurant

@router.get("/{restaurant_id}", status_code=200 ,response_model=RestaurantResponse)
async def get_restaurant(restaurant_id: UUID, db: get_db = Depends()):
    try: 
        restaurant = RestaurantService(db).get_by_id(restaurant_id)
        return restaurant
    except Exception as e:
        raise e

@router.patch("/{restaurant_id}")
async def update_restaurant(restaurant_id: UUID, db: get_db = Depends()):
    try:
        restaurant = RestaurantService(db).update(restaurant_id)
        return restaurant
    except Exception as e:
        raise e