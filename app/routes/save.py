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
    plantdata.user_id = current_user.id
    db.add(plantdata)
    db.commit()
    db.refresh(plantdata)
    return plantdata

@router.get('/post/me')
async def save_plant(current_user = Depends(get_current_active_user), db: Session = Depends(get_db)):
    get_user_data = db.query(DembeghaPost)
    db_result = get_user_data.filter(DembeghaPost.user_id == current_user.id).all()
    return db_result

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
    # plantdata.offerer_name = "current_user.firstName + ' ' + current_user.lastName" 
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
    "Books and Magazines",
    "Food and Grocery",
    "Sports and Outdoors",
    "Automotive",
]

image_urls = [
    "https://www.electronicspecifier.com/cms/images/inline-2018-03/wiresconnecting1.jpg",
    "https://img.freepik.com/free-photo/black-woman-trendy-grey-leather-jacket-posing-beige-background-studio-winter-autumn-fashion-look_273443-141.jpg",
    "https://c1.wallpaperflare.com/preview/152/978/370/garden-flowers-home-garden-shed.jpg",
    "https://thepointsguy.global.ssl.fastly.net/us/originals/2022/09/Cosmetics-and-beauty-rpoduct-flat-lay_Iryna-Veklich.jpg",
    "https://media.istockphoto.com/id/687165852/photo/toys.webp?b=1&s=170667a&w=0&k=20&c=aECJBVRGL3jNtrbiHOTMq1-5rSv3xeNUpZywEZYwvX4=",
    "https://img.freepik.com/free-photo/creative-composition-world-book-day_23-2148883765.jpg?size=626&ext=jpg&ga=GA1.1.1395880969.1709769600&semt=sph",
    "https://images.unsplash.com/photo-1542838132-92c53300491e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z3JvY2VyeXxlbnwwfHwwfHx8MA%3D%3D",
    "https://c4.wallpaperflare.com/wallpaper/176/1013/227/running-sports-shoes-outdoor-activities-wallpaper-preview.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRc8G6jnjll-aZ2prUZimjNetaonanodJQ8hQ&usqp=CAU",
]




@router.get("/catagory")
async def get_catagory():
    return {"cat": market_categories, "img": image_urls}


chapa = Chapa('CHASECK_TEST-Sgv4Pkoiu8lNu8YPOzUDW25rm5rYdzQ8', response_format='obj')

def pay(ret_url, fname, lname, amount):
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
async def get_catagory(ret_url,amount, current_user = Depends(get_current_active_user)):
    res = pay(ret_url, current_user.firstName, current_user.lastName, amount) 
    return res
