from fastapi import APIRouter
from fastapi_app.core.config import get_settings


settings = get_settings()

router = APIRouter(tags=["Home"])

# http://localhost:8000/api/v1
@router.get("/")
def get_hello():
    return {"Hello": settings.app_name}

# http://localhost:8000/api/v1/health
@router.get("/health")
def get_health():
    return {"status": "ok", "debug": settings.debug}

# http://localhost:8000/api/v1/company/xxx
# Path Parameters
@router.get("/company/{name}")
def get_company_info(name: str):
    name_valid = name.lower()
    return {"company_name": name_valid}

# http://localhost:8000/api/v1/company/search?name=Facebook&id=10
# Query Parameters
@router.get("/company/search/")
def search_company_info(name: str, id: int):
    name_valid = name.lower()
    return {"company_name": name_valid, "id": id}