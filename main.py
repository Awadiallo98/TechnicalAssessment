from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
import json

#  Initialize FastAPI app and Jinja2 templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load products from JSON file
with open("products.json") as f:
    products = json.load(f)

# Define the home route with filtering capabilities
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, query: Optional[str] = None, max_price: Optional[str] = Query(None)):
    filtered = products

    if query:
        q = query.lower()
        filtered = [
            p for p in filtered 
            if q in p["name"].lower() 
            or q in p["description"].lower() 
            or q in p["category"].lower()
        ]
    if max_price:
        try:
            max_price_val = float(max_price)
            filtered = [p for p in filtered if p["price"] <= max_price_val]
        except ValueError:
            pass

    return templates.TemplateResponse("index.html", {"request": request, "products": filtered})
