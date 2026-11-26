from fastapi import APIRouter, Depends
from src.login.dtos import LoginScheme
from src.db import get_db
from src.login.controller import login_user

user_login = APIRouter()

@user_login.get('/login')
def login(details: LoginScheme, db = Depends(get_db)):
    login_user(details, db)