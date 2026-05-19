#pages router
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Depends
from ..deps import get_db
from .. import crud, schemas


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")

@router.post("/items/")
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/items/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)

@router.post("/scans/")
def create_scan(scan: schemas.Scan, db: Session = Depends(get_db)):
    return crud.create_scan(db=db, scan=scan)

@router.get("/scans/")
def read_scans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_scans(db=db, skip=skip, limit=limit)

@router.post("/tokens/")
def create_token(token: schemas.Token, db: Session = Depends(get_db)):
    return crud.create_token(db=db, token=token)

    
@router.get("/tokens/")
def read_tokens(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tokens(db=db, skip=skip, limit=limit)