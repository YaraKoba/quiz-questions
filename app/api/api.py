from fastapi import APIRouter
from app.api.endpoint import questions

api_router = APIRouter()

api_router.include_router(questions.router, tags=['questions'])

