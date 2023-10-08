from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from configs.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"
    id= Column(UUID(as_uuid=True), primary_key=True, default=uuid4 ,nullable=False, unique=True)
    rating= Column(Integer, nullable=False)
    name= Column(String, nullable=False)
    site= Column(String, nullable=False)
    email= Column(String, nullable=False)
    phone= Column(String, nullable=False)
    street= Column(String, nullable=False)
    city= Column(String, nullable=False)
    state= Column(String, nullable=False)
    lat= Column(Float, nullable=False)
    ing= Column(Float, nullable=False)
