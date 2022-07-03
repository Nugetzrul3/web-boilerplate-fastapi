from sqlmodel import SQLModel, Field
from typing import Optional
from app import utils

class User(SQLModel, table=True):
    uname: str = Field(default=utils.gen_seq, primary_key=True)
    fname: str
    lname: Optional[str] = None
    description: Optional[str] = None
