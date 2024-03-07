from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError


from ..schema import schemas
from ..database.database import SessionLocal
from ..models.models import User
from ..helpers.hash import Hash
from ..helpers.token import Token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def get_user(phone: str, db: Session = next(get_db())):
    get_data = db.query(User)
    user_dict = get_data.filter(User.phone == phone).first()
    return user_dict

def authenticate_user(phone: str, password: str):
    user = get_user(phone)
    if not user:
        return False
    if not Hash.verify_password(password, user.password):
        return False
    return user

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

def phone_unverified(phone):
    unverified_account = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={'phone_verified':False , 'msg':"please verify your phone number", 'phone_number': phone},
        headers={"WWW-Authenticate": "Bearer"},
    )
    return unverified_account

def user_disabled(phone):
    disabled_account = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={'msg':"user has been disabled", 'phone_number': phone},
        headers={"WWW-Authenticate": "Bearer"},
    )
    return disabled_account

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = Token.decode(token)
        phone: str = payload.get("sub")
        if phone is None:
            raise credentials_exception
        token_data = schemas.TokenData(phone=phone)
    except JWTError:
        raise credentials_exception
    user = get_user(phone=token_data.phone)
    if user is None:
        raise credentials_exception
    # if not user.verified:
    #     raise phone_unverified(user.phone)
    # if user.disabled:
    #     raise user_disabled(user.phone)
    return user


async def get_current_active_user(current_user: schemas.UserSchema = Depends(get_current_user)):
    return current_user

