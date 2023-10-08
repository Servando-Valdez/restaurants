from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.restaurants import Restaurant
from schemas.restaurants import RestaurantRequest, UpdateRestaurantRequest
from uuid import uuid4, UUID
class AppService(object):
    def __init__(self, db: Session):
        self.db = db
class RestaurantService(AppService):

    def __init__(self, db):
        super().__init__(db)
        self.db = db
    
    def create(self, restaurant: RestaurantRequest):
        restaurant = restaurant.__dict__
        new_restaurant = Restaurant(**restaurant)
        self.db.add(new_restaurant)
        self.db.commit()
        self.db.refresh(new_restaurant)
        return new_restaurant
    
    def get_all(self):
        restaurants = self.db.query(Restaurant).all()
        if not restaurants:
            raise HTTPException(status_code=404, detail=f"No restaurants found")
        for restaurant in restaurants:
            restaurant.__dict__.pop("_sa_instance_state")
        return restaurants
    
    def get_by_id(self, restaurant_id: UUID):
        restaurant =  self.db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
        if not restaurant:
            raise HTTPException(status_code=404, detail=f"Restaurant with id {restaurant_id} not found")
        return restaurant
    
    def update(self, restaurant_id: UUID, new_data_restaurant: UpdateRestaurantRequest):
        new_data_restaurant = {key: value for key, value in new_data_restaurant.__dict__.items() if value is not None}
        restaurant = self.get_by_id(restaurant_id)

        for key, value in new_data_restaurant.items():
            setattr(restaurant, key, value)

        self.db.commit()
        self.db.refresh(restaurant)
        return restaurant
    
    def delete(self, restaurant_id: UUID):
        restaurant = self.get_by_id(restaurant_id)
        self.db.delete(restaurant)
        self.db.commit()
        return True