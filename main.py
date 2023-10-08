from fastapi import FastAPI

#routers
from routers import restaurants

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(restaurants.router)