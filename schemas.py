from pydantic import BaseModel


class AuthorCreateInput(BaseModel):
    name: str
    username: str
    picture: str
    country:str
    bio: str


class StandardOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str
