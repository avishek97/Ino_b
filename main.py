from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def main():
    print("Hello from ino!")

app = FastAPI()

app.middleware(
    CORSMiddleware,
    allow_origins=['https://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == "__main__":
    main()
