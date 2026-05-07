from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from app.models import UrlRequest
from app.store import url_store
from app.utils import generate_short_code

app = FastAPI()

@app.post("/shorten")
def shorten_url(request: UrlRequest):
    original_url = str(request.url)
    short_code = generate_short_code(original_url)

    if short_code in url_store:

        existing_url = url_store[short_code]["url"]

        if existing_url == original_url:

            return {
                "shorten_url":f"http://loalhost:8000/{short_code}"
            }

        raise HTTPException(
            status_code = 400,
            detail = "Hash collision occurred"
        )

    url_store[short_code] = {
        "url": original_url,
        "clicks":0
    }

    return{
        "short_url":
        f"http://loalhost:8000/{short_code}"
    }


@app.get("/{short_code}")
def redirect_url(short_code:str):

    if short_code not in url_store:
        raise HTTPException(
            status_code = 404,
            detail = "Short URL not found"
        )

    url_store[short_code][clicks]+=1

    original_url = url_store[short_code]["url"]

    return RedirectResponse(url=original_url)

@app.get("/status/{short_code}")
def get_stats(short_code:str):

        if short_code not in url_store:
            raise HTTPException(
                status_code = 404,
                detail = "Short URL not found"
            )

        return{
            "url":url_store[short_code]["url"],
            "clicks": url_store[short_code]["clicks"]
        }