# Run with:
#   .\.venv\Scripts\activate.bat
#   uvicorn app.app:app --reload
# Then open http://127.0.0.1:8000/ in the browser.

from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models
from .database import SessionLocal, engine

app = FastAPI()

# Serve everything under ./static at the URL prefix /static.
# This is what makes /static/js/scanner.js, /static/css/styles.css, etc. work.
app.mount("/static", StaticFiles(directory="static", check_dir=False), name="static")

# Templates live in ./templates; FastAPI/Jinja2 will look for index.html there.
templates = Jinja2Templates(directory="templates")

# Create all tables defined in models.py (subclasses of Base) the first time
# the app starts. Safe to call repeatedly — it only creates missing tables.
models.Base.metadata.create_all(bind=engine)


def get_db():
    """Yield a SQLAlchemy session for one request, then close it.

    FastAPI calls this for every endpoint that depends on it, so each request
    gets its own session and we don't leak connections.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Item(BaseModel):
    """Shape of the JSON the frontend sends to POST /items/.

    The browser code sends { "name": "<decoded QR text>" }. `description`
    and `price` are optional so we can extend later without breaking clients.
    """
    name: str
    description: Optional[str] = None
    price: Optional[float] = None


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # Jinja2Templates needs the template name plus a context dict that
    # includes `request` so the template can build URLs, etc.
    return templates.TemplateResponse(request, "index.html")


@app.post("/items/")
def create_item(item: Item, db: Session = Depends(get_db)):
    """Persist a scanned QR code as a row in the `items` table.

    1. FastAPI validates the JSON body against the Item Pydantic model.
    2. We build a SQLAlchemy ORM row using the model in app/models.py.
    3. add() stages the insert, commit() writes it to SQLite, refresh()
       reloads server-generated fields like the auto-increment id.
    """
    if not item.name:
        # Defensive check; Pydantic already requires `name`, but be explicit.
        raise HTTPException(status_code=400, detail="name is required")

    row = models.Item(name=item.name, description=item.description)
    db.add(row)
    db.commit()
    db.refresh(row)

    return {"id": row.id, "name": row.name}
