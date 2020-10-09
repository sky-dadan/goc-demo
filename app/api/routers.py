from fastapi import  APIRouter

router = APIRouter()

from app.api.trouble import  views
from app.api.department import views
from app.api.troubletype import views