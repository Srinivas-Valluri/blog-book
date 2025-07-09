from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    
    class Config:
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[ShowBlog] = []
    
    class Config:
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None