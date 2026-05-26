from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Depends, HTTPException
from ..deps import get_db
from .. import crud, schemas, models
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class ScanAndLinkResponse(BaseModel):
    scan: schemas.ScanBase
    item: schemas.ItemBase
    token: schemas.TokenWithRelations

    class Config:
        from_attributes = True

@router.get("/scan_and_link/", response_model=ScanAndLinkResponse)
def get_latest_scan(db: Session = Depends(get_db)):
    """Get the most recent scan with all its connected data"""
    latest_scan = db.query(models.Scan).order_by(models.Scan.id.desc()).first()
    if not latest_scan:
        raise HTTPException(status_code=404, detail="No scans found")
    
    latest_token = db.query(models.Token).filter(
        models.Token.scan_id == latest_scan.id
    ).order_by(models.Token.id.desc()).first()
    
    if not latest_token:
        raise HTTPException(status_code=404, detail="No tokens found for this scan")
    
    item = db.query(models.Item).filter(models.Item.id == latest_token.item_id).first()
    
    return ScanAndLinkResponse(
        scan=schemas.ScanBase.model_validate(latest_scan),
        item=schemas.ItemBase.model_validate(item),
        token=schemas.TokenWithRelations.model_validate(latest_token)
    )

@router.post("/scan_and_link/", response_model=ScanAndLinkResponse)
def scan_and_link(scan: schemas.Scan, db: Session = Depends(get_db)):
    db_scan = crud.create_scan(db, scan)
    db_item = crud.create_item(db, schemas.Item(name=scan.text, description=None))
    db_token = crud.create_token(db, schemas.Token(
        text=scan.text,
        source=scan.source,
        item_id=db_item.id,
        scan_id=db_scan.id,
        date=datetime.utcnow()
    ))

    # ✅ Return Pydantic models, not raw ORM
    return ScanAndLinkResponse(
        scan=schemas.Scan.model_validate(db_scan),
        item=schemas.Item.model_validate(db_item),
        token=schemas.Token.model_validate(db_token)
    )



@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")

@router.get("/items/{item_id}", status_code=200, response_model=schemas.ItemWithTokens)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific item with all its tokens and their scans"""
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/scans/{scan_id}", status_code=200, response_model=schemas.ScanWithTokens)
def read_scan(scan_id: int, db: Session = Depends(get_db)):
    """Get a specific scan with all its tokens and their items"""
    db_scan = db.query(models.Scan).filter(models.Scan.id == scan_id).first()
    if not db_scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    return db_scan

@router.get("/tokens/{token_id}", status_code=200, response_model=schemas.TokenWithRelations)
def read_token(token_id: int, db: Session = Depends(get_db)):
    """Get a specific token with its item and scan details"""
    db_token = db.query(models.Token).filter(models.Token.id == token_id).first()
    if not db_token:
        raise HTTPException(status_code=404, detail="Token not found")
    return db_token

@router.post("/items/", status_code=201, response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    existing = db.query(models.Item).filter(models.Item.name == item.name).first()
    if existing:
        # Return existing item instead of error
        return existing

    return crud.create_item(db=db, item=item)

@router.get("/items/", status_code=200, response_model=list[schemas.ItemWithTokens])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)

@router.post("/scans/", status_code=201, response_model=schemas.Scan)
def create_scan(scan: schemas.Scan, db: Session = Depends(get_db)):
    existing = db.query(models.Scan).filter(models.Scan.text == scan.text).first()
    if existing:
        # Return existing scan instead of error
        return existing

    return crud.create_scan(db=db, scan=scan)

@router.get("/scans/", response_model=list[schemas.ScanWithTokens])
def read_scans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_scans(db=db, skip=skip, limit=limit)


@router.post("/tokens/", status_code=201, response_model=schemas.Token)
def create_token(token: schemas.Token, db: Session = Depends(get_db)):
    # Use token.item_id and token.scan_id directly
    if token.item_id and not db.query(models.Item).filter(models.Item.id == token.item_id).first():
        raise HTTPException(status_code=404, detail="Item not found")
    if token.scan_id and not db.query(models.Scan).filter(models.Scan.id == token.scan_id).first():
        raise HTTPException(status_code=404, detail="Scan not found")

    db_token = models.Token(
        text=token.text,
        source=token.source,
        date=token.date,
        item_id=token.item_id,
        scan_id=token.scan_id
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

@router.get("/tokens/", status_code=200, response_model=list[schemas.TokenWithRelations])
def read_tokens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tokens(db=db, skip=skip, limit=limit)