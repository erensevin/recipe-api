from recipe_scrapers import scrape_me
from recipe_scrapers._exceptions import WebsiteNotImplementedError
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()
security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    username = os.getenv("AUTH_USERNAME")
    password = os.getenv("AUTH_PASSWORD")
    
    if not username or not password:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Authentication not configured properly"
        )
    
    if credentials.username != username or credentials.password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe Scraper API!"}

@app.post("/scrape")
def scrape_recipe(request: dict, username: str = Depends(authenticate)) -> dict:
    """
    Scrape recipe data from a given URL.

    Args:
        request (dict): A dictionary containing the URL to scrape. Must have a 'url' key.

    Returns:
        dict: A dictionary containing either:
            - On success: 'title' (str) and 'ingredients' (list) of the recipe
            - On error: 'error' (str) with error message describing what went wrong

    Raises:
        Does not raise exceptions directly, but catches and returns error messages for:
        - WebsiteNotImplementedError: When the website is not supported for scraping
        - Exception: Any other unexpected errors during scraping
    """
    try:
        scraper = scrape_me(request["url"])
        return {
            "title": scraper.title(),
            "ingredients": scraper.ingredients(),
        }
    except WebsiteNotImplementedError as e:
        return {"error": "Website not implemented for scraping yet"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)