from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependency.dependency import get_current_active_user
from ..models.models import User
from ..dependency.dependency import get_db
from ..helpers.datecalculator import has_passed

router = APIRouter(
    prefix="/plan",
    tags=["Subscription Route"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)




@router.post('/subscribe')
async def generate_link_for_subscription(current_user = Depends(get_current_active_user)):
    plan_expired = has_passed(current_user.plan_expire_date)
    return 'abdc'


@router.post('/verify')
async def webhook_for_subscription(ref_txt: str ,current_user = Depends(get_current_active_user), db: Session = Depends(get_db)):
    db.query(User).filter(User.phone == current_user.phone).update({'plan_expire_date': '', 'plan':'pro'})
    db.commit()
    pass


@router.post('/webhook')
async def webhook_for_subscription(ref_txt: str ,current_user = Depends(get_current_active_user), db: Session = Depends(get_db)):
    db.query(User).filter(User.phone == current_user.phone).update({'plan_expire_date': True, 'plan':'pro'})
    db.commit()
    pass