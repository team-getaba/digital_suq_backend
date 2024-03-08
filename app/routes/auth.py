from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

# local imports 
from ..schema.schemas import UserSchema
from ..dependency.dependency import get_db, authenticate_user 
from ..models.models import User
from ..helpers.hash import Hash 
from ..helpers.token import Token


router = APIRouter(
    prefix="",
    tags=["Authentication"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# example = 098049013366


@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(
        form_data.username, form_data.password)
    if not user:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Incorrect phone number or password",
        #     headers={"WWW-Authenticate": "Bearer"},
        # )
        return {'msg': 'Incorrect phone number or password'}
    access_token = Token.create_access_token(data={"sub": user.phone})
    return {"access_token": access_token, "token_type": "bearer", "phone_verified": user.verified, "role": user.role, "user_id": user.id, 'fname': user.firstName, 'lname': user.lastName}



@router.post('/signup')
async def signup(
    firstName: str = Form(...),
    lastName: str = Form(...),
    phone: str = Form(...),
    location: str = Form(...),
    role: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    get_user_data = db.query(User)
    db_result = get_user_data.filter(User.phone == phone).first()
    user = UserSchema(
        firstName=firstName,
        lastName=lastName,
        phone=phone,
        role=role,
        location=location,
        password=Hash.hash_password(password)
    )
    if not db_result:
        signupdata = User(**jsonable_encoder(user))
        db.add(signupdata)
        db.commit()
        db.refresh(signupdata)
        access_token = Token.create_access_token(data={"sub": signupdata.phone})
        return {"access_token": access_token, "token_type": "bearer", "phone_verified": False, "role": user.role, 'fname': user.firstName, 'lname': user.lastName}
    return {'detail': 'phone number already exists'}



