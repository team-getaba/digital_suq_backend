from fastapi import APIRouter

# local imports 
from ..schema.signup import SignUpSchema


router = APIRouter(
    prefix="/signup",
    tags=["signup route"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post('')
async def signup(signup: SignUpSchema):
    return signup