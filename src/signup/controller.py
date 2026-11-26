from src.signup.dtos import UserSchema
from sqlalchemy.orm import Session
from src.model import UserModel

def user_signup(details: UserSchema, db: Session):
    user_data = details.model_dump()
    new_user = UserModel(name = user_data['name'], email = user_data['email'], password = user_data['password'], confirm_password = user_data['confirm_password'])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": 200, "message": "User Signup "}