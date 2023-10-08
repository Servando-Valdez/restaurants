from fastapi import APIRouter

router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
)

@router.get("/")
async def get_all_restaurants():
    return {"message": "Get all restaurants"}