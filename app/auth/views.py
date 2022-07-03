from sqlmodel import Session, select
from ..models import engine, User
from pydantic import BaseModel
from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/user")

class UserBody(BaseModel):
    uname: str
    fname: str
    lname: Optional[str] = None
    description: Optional[str] = None

@router.post("/add")
async def add(user: UserBody):
    with Session(engine) as session:
        new_user = User(
            uname=user.uname, fname=user.fname,
            lname=user.lname, description=user.description
        )

        session.add(new_user)
        session.commit()

    return {
        "success": True
    }

@router.get("/get")
async def get(uname: str):
    with Session(engine) as session:
        statement = select(User).where(User.uname == uname)

        if (user := session.exec(statement).first()):

            return {
                "username": user.uname,
                "first_name": user.fname,
                "last_name": user.lname,
                "description": user.description
            }

        return {
            "error": "User not found"
        }


