from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session

from ..dependency.dependency import get_current_active_user
from ..models.models import UserPlants, User
from ..dependency.dependency import get_db
from ..helpers.token import Token

router = APIRouter(
    prefix="/user",
    tags=["User Details"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/account")
async def get_currunt_user(current_user = Depends(get_current_active_user)):
    return current_user

dummy_code_list = [1423, 2456, 6789, 1498, 1164, 7234]

def phone_verified(phone):
    access_token = Token.create_access_token(data={"sub": phone})
    return {
        "phone_verified": True,
        "msg": 'phone number verified successfully',
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.post('/verify')
async def verify_phone_number(phone: str = Form(...), code: int = Form(...),  db: Session = Depends(get_db)):
    get_user_data = db.query(User)
    db_result = get_user_data.filter(User.phone == phone).first()
    if db_result:
        if code in dummy_code_list:
            if not db_result.verified:
                db.query(User).filter(User.phone == phone).update({'verified': True})
                db.commit()
            return phone_verified(phone)
        else:
            return {'detail': 'incorrect code supplied'}
    return {'detail': 'phone number doesnt exists'}
