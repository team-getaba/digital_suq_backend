from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from chapa import Chapa
import uuid



from ..dependency.dependency import get_current_active_user
from ..schema.schemas import UserPlantSchema, DembeghaPostSchema, BaleSuqOfferSchma
from ..dependency.dependency import get_db
from ..models.models import UserPlants, DembeghaPost, BaleSuqOffer
from ..settings.settings import FREE_TRIAL_NUMBER, TEST_MODE
from ..helpers.datecalculator import has_passed

router = APIRouter(
    prefix="",
    tags=["Main point Data"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post('/post')
async def save_plant(plant: DembeghaPostSchema, current_user = Depends(get_current_active_user), db: Session = Depends(get_db)):
    plantdata = DembeghaPost(**jsonable_encoder(plant))
    plantdata.userid = current_user.id
    db.add(plantdata)
    db.commit()
    db.refresh(plantdata)
    return plantdata

@router.get('/post/me')
async def save_plant(current_user = Depends(get_current_active_user), db: Session = Depends(get_db)):
    
    return ""

@router.get("/catagory/{catname}")
async def get_catagory(catname, db: Session = Depends(get_db)):
    get_user_data = db.query(DembeghaPost)
    db_result = get_user_data.filter(DembeghaPost.catagory == catname).all()
    return db_result

@router.get("/catagory/{catname}/{post_id}")
async def get_catagory(catname, post_id, db: Session = Depends(get_db)):
    get_user_data = db.query(DembeghaPost)
    db_result = get_user_data.filter(DembeghaPost.catagory == catname).all()
    return db_result

@router.get("/chat/{chat_id}")
async def get_catagory(catname, post_id, db: Session = Depends(get_db)):
    get_user_data = db.query(DembeghaPost)
    db_result = get_user_data.filter(DembeghaPost.catagory == catname).all()
    return db_result


@router.get("/catagory/all")
async def get_catagory(db: Session = Depends(get_db)):
    get_user_data = db.query(DembeghaPost)
    db_result = get_user_data.all()
    return db_result


@router.post('/offer')
async def save_plant(plant: BaleSuqOfferSchma, current_user = Depends(get_current_active_user), db: Session = Depends(get_db)):
    plantdata = BaleSuqOffer(**jsonable_encoder(plant))
    plantdata.offerer_id = current_user.id
    db.add(plantdata)
    db.commit()
    db.refresh(plantdata)
    return plantdata


@router.get("/post/offer/{post_id}")
async def get_catagory(post_id, db: Session = Depends(get_db)):
    get_user_data = db.query(BaleSuqOffer)
    db_result = get_user_data.filter(BaleSuqOffer.post_id == post_id).all()
    return db_result


@router.get("/chat/{chat_id}")
async def get_catagory(offer_id, db: Session = Depends(get_db)):
    get_user_data = db.query(DembeghaPost)
    db_result = get_user_data.filter(DembeghaPost.offerer_id == offer_id).all()
    return db_result


market_categories = [
    "Electronics",
    "Fashion",
    "Home and Garden",
    "Health and Beauty",
    "Toys and Games",
    "Sports and Outdoors",
    "Books and Magazines",
    "Food and Grocery",
    "Automotive",
    "Pet Supplies"
]

image_urls = [
    "https://via.placeholder.com/150x150.png?text=Electronics",
    "https://via.placeholder.com/150x150.png?text=Fashion",
    "https://via.placeholder.com/150x150.png?text=Home+Garden",
    "https://via.placeholder.com/150x150.png?text=Health+Beauty",
    "https://via.placeholder.com/150x150.png?text=Toys+Games",
    "https://via.placeholder.com/150x150.png?text=Sports+Outdoors",
    "https://via.placeholder.com/150x150.png?text=Books+Magazines",
    "https://via.placeholder.com/150x150.png?text=Food+Grocery",
    "https://via.placeholder.com/150x150.png?text=Automotive",
    "https://via.placeholder.com/150x150.png?text=Pet+Supplies"
]




@router.get("/catagory")
async def get_catagory():
    return {"cat": market_categories, "img": image_urls}


chapa = Chapa('CHASECK_TEST-Sgv4Pkoiu8lNu8YPOzUDW25rm5rYdzQ8', response_format='obj')

def pay(ret_url, fname, lname, amount=100):
    data = {
        'email': "profesornaoltena@gmail.com",
        'amount': amount,
        'first_name': fname,
        'last_name': lname,
        'tx_ref': 'adbc' + str(uuid.uuid4()),
        # optional
        'return_url': ret_url,
        'callback_url': '',
        'customization': {
            'title': 'payment',
            'description': 'Payment for your services',
        }
    }

 
    response = chapa.initialize(**data)

    print(response)
    return response
# # Another Implementation
# chapa = Chapa('<your_api_key>', response_format='obj')
# response = chapa.initialize(**data)
# # notice how the response is an object
# print(response.data.checkout_url)


# # How to verify a transaction
# response = chapa.verify('<your-unique-transaction-id>')


@router.get("/pay")
async def get_catagory(ret_url,current_user = Depends(get_current_active_user)):
    res = pay(ret_url, current_user.firstName, current_user.lastName) 
    return res
