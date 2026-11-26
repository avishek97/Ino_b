from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.signup.router import signup_router
from src.login.router import user_login
from src.db import Base, engine

Base.metadata.create_all(engine)
def main():
    print("Hello from ino!")

origins = [
    "http://localhost:3000",  # Replace with your frontend URL(s)
    "http://127.0.0.1:8000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(signup_router)
app.include_router(user_login)
