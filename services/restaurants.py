from sqlalchemy.orm import Session
from models.restaurants import Restaurant
from uuid import uuid4
class DBSessionContext(object):
    def __init__(self, db: Session):
        self.db = db

class AppService(DBSessionContext):
    pass

class RestautantService(AppService):

    def __init__(self, db):
        self.db = db
    
    def create(self, restaurant):
        new_restaurant = Restaurant(**restaurant)
        self.db.add(new_restaurant)
        self.db.commit()
        self.db.refresh(new_restaurant)
        return new_restaurant
    
    def get_all(self):
        return self.db.query(Restaurant).all()