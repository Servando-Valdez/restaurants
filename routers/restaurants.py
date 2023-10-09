from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, Response, Query
import traceback
from schemas.restaurants import RestaurantRequest, RestaurantResponse, UpdateRestaurantRequest
from configs.database import get_db
from services.restaurants import RestaurantService
from uuid import UUID
from models.restaurants import Restaurant


router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
)

@router.get("/restaurants/statistics")
async def get_restaurant_statistics(latitude: float = Query(..., description="Latitude of the center of the circle"),
                                    longitude: float = Query(..., description="Longitude of the center of the circle"),
                                    radius: float = Query(..., description="Radius in METERS"),
                                    db: get_db = Depends()
                                    ):
    try:
        result = RestaurantService(db).get_statics(latitude, longitude, radius)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", status_code=200 ,response_model=List[RestaurantResponse])
async def get_all_restaurants(db: get_db = Depends()):
    print("get_all_restaurants")
    try:
        restaurants = RestaurantService(db).get_all()
        return restaurants
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Uncontrolled error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/", status_code=201, response_model=RestaurantResponse)
async def create_restaurant(item: RestaurantRequest, db: get_db = Depends()):
    restaurant = RestaurantService(db).create(item)
    return restaurant

@router.get("/{restaurant_id}", status_code=200 ,response_model=RestaurantResponse)
async def get_restaurant(restaurant_id: UUID, db: get_db = Depends()):
    try: 
        restaurant = RestaurantService(db).get_by_id(restaurant_id)
        return restaurant
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Uncontrolled error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch("/{restaurant_id}", status_code=200, response_model=RestaurantResponse)
async def update_restaurant(restaurant_id: UUID, item: UpdateRestaurantRequest ,db: get_db = Depends()):
    try:
        restaurant = RestaurantService(db).update(restaurant_id, item)
        return restaurant
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Uncontrolled error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{restaurant_id}", status_code=204)
async def delete_restaurant(restaurant_id: UUID, db: get_db = Depends()):
    try:
        RestaurantService(db).delete(restaurant_id)
        return Response(status_code=204)
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Uncontrolled error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")