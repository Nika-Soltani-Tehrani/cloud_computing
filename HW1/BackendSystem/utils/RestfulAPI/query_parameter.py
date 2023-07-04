from pydantic import BaseModel


class PostDetail(BaseModel):
    description: str
    photoURL: str
    emailAddress: str
