from src.login.dtos import LoginScheme
from sqlalchemy.orm import Session
from src.model import UserModel

def login_user(details: LoginScheme, db: Session):
    user = details.model_dump()
    result = db.query(UserModel).filter(user['email'] == UserModel.email).first()
    if user['password'] == result.password:
        return {"status": 200, "message": "Logged In ", "id": result.id}
    else:
        return {"status": 401, "message": "Error in login"}