from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

#Post Schema
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass    

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime 

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
#    title: str
#    content: str
#    published: bool = True    
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
    
#User Schema
class UserCreate(BaseModel):
    email: EmailStr
    password: str

#Authentication Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

#Vote/Like Schema
class Vote(BaseModel):
    post_id: str
    dir: conint(le=1) #less than or equal 1  
