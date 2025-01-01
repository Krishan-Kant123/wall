from popular import popular
from search import search
from tags_wall import tags
from tag_ext import extract_tags
from fastapi import FastAPI


import requests

import json

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware





middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)



@app.get("/")
async def main():
    return extract_tags()

@app.get('/popular/{pgno}')
async def main(pgno:int=1):
    return popular(pgno)

@app.get('/category/{pgno}/{tag}')
async def main(pgno:int,tag:str):
    return tags(pgno,tag)

@app.get('/search/{query}')
async def main(query:str):
    return search(query)