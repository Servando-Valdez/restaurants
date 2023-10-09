import math
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.restaurants import Restaurant
from schemas.restaurants import RestaurantRequest, UpdateRestaurantRequest
from uuid import uuid4, UUID
import numpy as np
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
    
    def get_statics(self, latitude: float, longitude: float, radius: float):
        restaurants = self.get_all()
        ratings = []
        nearby_restaurants = []
        #convert radius to kilometers
        radius = radius / 1000
        for restaurant in restaurants:
            ratings.append(restaurant.rating)
            distancia = self.calculate_distance(longitude, latitude, restaurant.lng, restaurant.lat)
            if distancia <= radius:
                nearby_restaurants.append(restaurant)
        result = {
            "count": len(nearby_restaurants),
            "avg": np.mean(ratings),
            "std": np.std(ratings),
        }
        return result

    def calculate_distance(self, lon1, lat1, lon2, lat2):
        # Earth's radius in kilometers
        earth_radius = 6371.0
        
        # Convert degrees to radians
        lon1 = math.radians(lon1)
        lat1 = math.radians(lat1)
        lon2 = math.radians(lon2)
        lat2 = math.radians(lat2)
        
        # Differences in longitude and latitude
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        # Haversine distance formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        # Calculate the distance in kilometers
        distance = earth_radius * c
        
        return distance