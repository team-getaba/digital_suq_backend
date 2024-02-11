from pydantic import BaseModel


class SignUpSchema(BaseModel):
    FirstName: str
    LastName: str 
    Phone: str 
    Password: str 
    Email: str = None 
    Gender: str = None
