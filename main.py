from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# local imports
from app.routes import auth, save, user
from app.models import models
from app.database.database import engine


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(save.router)