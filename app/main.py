from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#For database (sqlachemy)
from .database import engine

#For connecting other files
from . import models
from .routers import post, user, auth, vote
from .config import settings

#Not using anymore because of alembic
#models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Alternative Database
#my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

#def find_post(id):
#    for p in my_posts:
#        if p["id"] == id:
#            return p

#def find_index_post(id):
#    for i, p in enumerate(my_posts):
#        if p['id'] == id:
#            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#Methods
@app.get("/")
def root():
    return {"message": "Welcome to my API"}




    