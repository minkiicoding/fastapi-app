from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_app.api.router import api_router


app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# http://localhost:8000/api/v1
app.include_router(api_router, prefix="/api/v1")