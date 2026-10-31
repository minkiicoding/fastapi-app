from fastapi import APIRouter
from fastapi_app.modules.home.router import router as home_router
from fastapi_app.modules.auth.router import router as auth_router
from fastapi_app.modules.products.router import router as products_router

api_router = APIRouter()
api_router.include_router(home_router)
api_router.include_router(auth_router)
api_router.include_router(products_router)
