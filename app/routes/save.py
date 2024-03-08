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
    "Sports and Outdoors",
    "Books and Magazines",
    "Food and Grocery",
    "Automotive",
    "Pet Supplies"
]

image_urls = [
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fbridgeways.org%2Fwp-content%2Fuploads%2F2023%2F01%2FThe-Advantages-of-Outsourcing-Electronics-Assembly-to-Contract-Manufacturers.jpg&tbnid=Rs5d2Fq6pc_lYM&vet=12ahUKEwirg7-siuSEAxWNU6QEHXcWASEQMygTegUIARCYAQ..i&imgrefurl=https%3A%2F%2Fbridgeways.org%2Foutsourcing-your-electronics-manufacturing%2F&docid=aR8pOIuqY_SpeM&w=1280&h=720&q=electronics&ved=2ahUKEwirg7-siuSEAxWNU6QEHXcWASEQMygTegUIARCYAQ",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcontent.ngv.vic.gov.au%2Fcol-images%2Fapi%2FFb108875%2F1920&tbnid=2D1AbF2WLeXpIM&vet=12ahUKEwiYxarliuSEAxVPVaQEHYLVDyQQMygZegUIARCoAQ..i&imgrefurl=https%3A%2F%2Fwww.ngv.vic.gov.au%2Fexplore%2Fcollection%2Ffashion-textiles%2F&docid=zvBXycq9JyJ1pM&w=1920&h=1455&q=Fashion&ved=2ahUKEwiYxarliuSEAxVPVaQEHYLVDyQQMygZegUIARCoAQ",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Ftownsquare.media%2Fsite%2F692%2Ffiles%2F2019%2F03%2FGettyImages-9201114321.jpg%3Fw%3D980%26q%3D75&tbnid=-vs_052-kI_JGM&vet=12ahUKEwjUqJ_0iuSEAxX9WaQEHW01AEEQMyg3egUIARDvAQ..i&imgrefurl=https%3A%2F%2Fwjimam.com%2Flansing-home-garden-show-this-weekend%2F&docid=JyDzOBYF0EETXM&w=980&h=651&q=Home%20and%20Garden&ved=2ahUKEwjUqJ_0iuSEAxX9WaQEHW01AEEQMyg3egUIARDvAQ",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fthepointsguy.global.ssl.fastly.net%2Fus%2Foriginals%2F2022%2F09%2FCosmetics-and-beauty-rpoduct-flat-lay_Iryna-Veklich.jpg&tbnid=AgVX2Z_9UPab1M&vet=12ahUKEwiqxs2Ni-SEAxUVlycCHRJUD6oQMygMegUIARCIAQ..i&imgrefurl=https%3A%2F%2Fthepointsguy.com%2Fguide%2Ftsa-approved-health-and-beauty%2F&docid=-F5ebPVbGqtIwM&w=1600&h=1067&q=Health%20and%20Beauty&ved=2ahUKEwiqxs2Ni-SEAxUVlycCHRJUD6oQMygMegUIARCIAQ",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.shopify.com%2Fs%2Ffiles%2F1%2F0037%2F8008%2F3782%2Ffiles%2FToys_Banner_3_1024x1024.png%3Fv%3D1689290982&tbnid=zyt-jRp30W57vM&vet=12ahUKEwijk76ii-SEAxV8daQEHd-7CYMQMyg0egUIARDlAQ..i&imgrefurl=https%3A%2F%2Fartofthemovies.co.uk%2Fblogs%2Foriginal-movie-posters%2Ftoy-stories-toys-and-games-in-movies&docid=Mo8ldrKw2T19dM&w=1024&h=513&q=Toys%20and%20Games&ved=2ahUKEwijk76ii-SEAxV8daQEHd-7CYMQMyg0egUIARDlAQ",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fsportstarsmag.com%2Fwp-content%2Fuploads%2F2019%2F04%2Fround-2086759_640.jpg&tbnid=gKgUqc26ixHTqM&vet=12ahUKEwi7o9S9i-SEAxWJlycCHVoTC44QMygDegQIARBP..i&imgrefurl=https%3A%2F%2Fsportstarsmag.com%2F2019%2F04%2F3-best-outdoor-sports-for-beginners&docid=Bbx_6FFjNPEexM&w=600&h=398&q=Sports%20and%20Outdoors&ved=2ahUKEwi7o9S9i-SEAxWJlycCHVoTC44QMygDegQIARBP",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Flive.cdn.renderosity.com%2Fmarketplace%2Fproducts%2F99797%2Ffull_e5ca8d7c6b6da5356e973f21c67b1f59.jpg&tbnid=Ee5ihPX85ztgrM&vet=12ahUKEwi-9O7Ni-SEAxU3TKQEHbzHBdsQMygIegQIARBc..i&imgrefurl=https%3A%2F%2Fwww.renderosity.com%2Fmarketplace%2Fproducts%2F99797%2Fbooks-and-magazines&docid=hNFBA3VoMW6A1M&w=711&h=400&q=Books%20and%20Magazines&ved=2ahUKEwi-9O7Ni-SEAxU3TKQEHbzHBdsQMygIegQIARBc",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fs3.amazonaws.com%2Fsecretsaucefiles%2Fphotos%2Fimages%2F000%2F109%2F800%2Flarge%2Fe-grocery-amazon-hed-2013.jpg%3F1485376278&tbnid=NI70lE6xnHUT3M&vet=12ahUKEwi4r8jii-SEAxUvQKQEHfpVA3QQMygEegQIARB7..i&imgrefurl=https%3A%2F%2Fspoonuniversity.com%2Flifestyle%2Fgrocery-store-delivery-options&docid=gc90oGqVluUIHM&w=652&h=367&q=food%20and%20grocery&ved=2ahUKEwi4r8jii-SEAxUvQKQEHfpVA3QQMygEegQIARB7",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.electronicspecifier.com%2Fcms%2Fimages%2Finline-2018-03%2Fwiresconnecting1.jpg&tbnid=iI-iffSJ1NELqM&vet=10CHwQMyigAWoXChMI6IKQ8ovkhAMVAAAAAB0AAAAAEAM..i&imgrefurl=https%3A%2F%2Fwww.electronicspecifier.com%2Fnews%2Fanalysis%2Fautomotive-servicing-in-the-era-of-the-electronic-car&docid=V_1eNpK3wIFa_M&w=800&h=503&q=Automotive&ved=0CHwQMyigAWoXChMI6IKQ8ovkhAMVAAAAAB0AAAAAEAM",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.retailmba.com%2Fwp-content%2Fuploads%2F2023%2F11%2Fwholesale-pet-products.jpeg&tbnid=V3UjEJxu4isLIM&vet=12ahUKEwiH-fShjOSEAxXalScCHQsYANYQMygDegQIARB4..i&imgrefurl=https%3A%2F%2Fwww.retailmba.com%2Fwholesale-pet-supplies%2F&docid=Ahnb3kypMLak2M&w=1000&h=667&q=Pet%20Supplies&ved=2ahUKEwiH-fShjOSEAxXalScCHQsYANYQMygDegQIARB4"
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
