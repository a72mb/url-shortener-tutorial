
import secrets #type:ignore
import validators # type:ignore
from fastapi import Depends, FastAPI, HTTPException # type: ignore
from sqlalchemy.orm import Session #type:ignore
from . import schemas


app = FastAPI()

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

@app.get("/")
def read_root():
    return "Welcome to the URL shortener API :)"

@app.post("/url")
def create_url(url:schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
    return f"TDO: Create database entry for {url.target_url}"
'''
@app.get("/{url_key}")
@app.get("/admin/{secret_key}")
@app.delete("/admin/{secret_key}")
'''