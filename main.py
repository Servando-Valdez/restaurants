from fastapi import FastAPI
from configs.database import create_tables
#routers
from routers import restaurants
from models.restaurants import Restaurant

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

create_tables()
# Base.metadata.create_all(bind=engine)

app.include_router(restaurants.router)