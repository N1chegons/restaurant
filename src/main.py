from fastapi import FastAPI
from src.auth.router import router as auth_router
from src.auth.user_router import router as user_router
# from src.restaurant.router import router as restaurant_router

app = FastAPI()


# router
app.include_router(user_router)
app.include_router(auth_router)
# app.include_router(restaurant_router)
