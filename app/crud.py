# crud.py - CRUD operations for the database
from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas

# ---- Item operations ----
def create_item(db: Session, item: schemas.Item):
    db_item = models.Item(
        name=item.name,
        description=item.description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()


# ---- Scan operations ----
def create_scan(db: Session, scan: schemas.Scan):
    db_scan = models.Scan(
        text=scan.text,
        source=scan.source, 
        date=datetime.utcnow(),
    )
    db.add(db_scan)
    db.commit()
    db.refresh(db_scan)
    return db_scan

def get_scans(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Scan).offset(skip).limit(limit).all()


# ---- Token operations ----
def create_token(db: Session, token: schemas.Token):
    db_token = models.Token(
        text=token.text,
        source=token.source,
        date=datetime.fromisoformat(token.date),
        item_id=token.item_id,
        scan_id=token.scan_id,
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def get_tokens(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Token).offset(skip).limit(limit).all()