from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse, Response

app = FastAPI()

def wsgi_app(environ, start_response):
    data = b"Hello, World!\n"
    start_response(
        "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
    )
    return iter([data])


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
    