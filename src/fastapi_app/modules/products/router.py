from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


products = [
    {"id": 1, "name": "Mouse", "price": 590, "stock": 10},
    {"id": 2, "name": "Keyboard", "price": 1290, "stock": 5},
    {"id": 3, "name": "Monitor", "price": 4990, "stock": 2},
]


class ProductCreate(BaseModel):
    name: str
    price: int
    stock: int


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def get_products():
    return products


@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product


@router.post("/", status_code=201)
def create_product(product: ProductCreate):
    new_product = {
        "id": max((item["id"] for item in products), default=0) + 1,
        **product.model_dump(),
    }
    products.append(new_product)
    return {"message": "success"}
