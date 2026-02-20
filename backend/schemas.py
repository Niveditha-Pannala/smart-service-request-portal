from pydantic import BaseModel

class Request(BaseModel):
    title: str
    category: str
    description: str
    priority: str
    name: str
    email: str