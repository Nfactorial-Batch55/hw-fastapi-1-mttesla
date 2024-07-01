from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse, JSONResponse, Response
from math import factorial

app = FastAPI()

"""
@app.get("/")
def read_root():
    return {"Hello": "World"}
"""

@app.get('/ping', response_class=PlainTextResponse)
async def ping():
    return 'pong'


@app.get('/info', response_class=JSONResponse)
async def info(request: Request):
    return {
        "method": request.method,
        'url': str(request.url),
        'protocol': request.scope['type'],
    }
    
    
@app.get('/', response_class=JSONResponse)
async def message():
    return {'message': "Hello, nfactorial!",}


@app.post('/meaning-of-life', response_class=JSONResponse)
async def message_post():
    return {"meaning": "42"}


@app.get('/{num}')
async def message_factorial(num: int):
    result = factorial(num)
    return {"nfactorial": result}


