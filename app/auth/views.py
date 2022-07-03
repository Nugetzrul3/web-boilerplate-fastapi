from sqlmodel import Session, select
from ..models import engine, User
from pydantic import BaseModel
from fastapi import APIRouter
from typing import Optional
from ..models import Hobby
from .. import utils

router = APIRouter(prefix="/user")

class UserBody(BaseModel):
    uname: str
    fname: str
    lname: Optional[str] = None
    description: Optional[str] = None

@router.post("/add")
async def add(user: UserBody):
    result = {"data": {}, "error": None}
    with Session(engine) as session:
        statement = select(User).where(User.uname == user.uname)
        results = session.exec(statement)

        if not results.first():

            new_user = User(
                uname=user.uname, fname=user.fname,
                lname=user.lname, description=user.description
            )

            session.add(new_user)
            session.commit()

            result["data"] = {
                "success": True
            }

            return result

        result["error"] = "User already exists"

        return result

@router.get("/get")
async def get(uname: str):
    result = {"data": {}, "error": None}
    with Session(engine) as session:
        statement = select(User).where(User.uname == uname)

        if (user := session.exec(statement).first()):

            result["data"] = {
                "username": user.uname,
                "first_name": user.fname,
                "last_name": user.lname,
                "description": user.description
            }

            return result

        result["error"] = "User not found"

        return result

class HobbyBody(BaseModel):
    hobby_name: str
    hobby_desc: Optional[str]
    uname: str

@router.post("/add_hobby")
async def add_hobby(hobby: HobbyBody):
    result = {"data": {}, "error": None}
    with Session(engine) as session:
        statement = select(User).where(User.uname == hobby.uname)

        if (user := session.exec(statement).first()):
            new_hobby = Hobby(
                hobby_id=utils.gen_seq(),
                hobby_name=hobby.hobby_name,
                hobby_desc=hobby.hobby_desc,
                uname=hobby.uname
            )

            session.add(new_hobby)
            session.commit()

            result["data"] = {
                "success": True
            }

            return result

        result["error"] = "User not found"

        return result

