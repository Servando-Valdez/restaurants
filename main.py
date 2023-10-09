from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs.database import create_tables
#routers
from routers import restaurants
from models.restaurants import Restaurant

app = FastAPI()

# origins = [
#     "http://localhost:8005/",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
async def root():
    return {"message": "Hello World"}

create_tables()
# Base.metadata.create_all(bind=engine)

app.include_router(restaurants.router)