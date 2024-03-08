from pydantic import BaseModel
from typing import List, Union



class UserSchema(BaseModel):
    firstName: str
    lastName: str 
    phone: str 
    role: str
    location: str
    password: str 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    phone: Union[str, None] = None


class plantDetails(BaseModel):
    cause: str = None
    prevention: str = None
    highlight: str = None

class lableimg(BaseModel):
    x_start: int = None
    y_start: int = None
    lable_width: int = None
    lable_height: int = None
    img_width: int = None
    img_height: int = None


class UserPlantSchema(BaseModel):
    imgurl: str
    lable: Union[lableimg, None]
    disease: str
    details: Union[plantDetails, None]
    deleted: bool = False

class DembeghaPostSchema(BaseModel):
    detail: str
    user_id: int
    catagory: str
    product_name: str
    location: str
    price_range: str
    img: str

class BaleSuqOfferSchma(BaseModel):
    poster_id: str
    post_id: str
    location: str
    details: str
    offerer_name: str
    price: str
    offerer_id: str
    
 

