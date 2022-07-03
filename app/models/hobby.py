from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Hobby(SQLModel, table=True):
    hobby_id: str = Field(primary_key=True)
    hobby_name: str
    hobby_desc: Optional[str] = None

    uname: str = Field(default=None, foreign_key="user.uname")
    user: "User" = Relationship(back_populates="uname")
