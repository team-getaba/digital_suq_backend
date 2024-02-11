from fastapi import FastAPI
# local imports
from app.routes import signup 

app = FastAPI()

app.include_router(signup.router)


