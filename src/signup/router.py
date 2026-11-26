from fastapi import APIRouter, Depends
from src.signup.dtos import UserSchema
from src.signup.controller import user_signup
from src.db import get_db

signup_router = APIRouter()

@signup_router.post('/signup')
def signup(details: UserSchema, db = Depends(get_db)):
    user_signup(details, db)
