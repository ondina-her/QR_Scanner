# crud.py - CRUD operations for the simplified database structure
from sqlalchemy.orm import Session, selectinload
from datetime import datetime
from . import models, schemas

UNSET = object()

# ==========================================
# ITEM OPERATIONS
# ==========================================

def create_item(db: Session, item: schemas.Item):
    """
    Checks if an item with the given QR name/text already exists.
    If it exists, it returns it; otherwise, creates a new one.
    """
    existing = db.query(models.Item).filter(models.Item.name == item.name).first()
    if existing:
        return existing

    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of items along with their nested history of scans.
    Optimized with selectinload for efficient database fetching.
    """
    return (
        db.query(models.Item)
        .options(selectinload(models.Item.scans))
        .order_by(models.Item.id.desc())  # Newest items first
        .offset(skip)
        .limit(limit)
        .all()
    )

#Update item
def update_item(db: Session, item_id: int, new_name: str | None = UNSET, new_description: str | None = UNSET):
    """
    Updates an existing item's name and/or description.
    Uses UNSET to distinguish omitted fields from explicit null values.
    If the item doesn't exist, returns None.
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        return None

    if new_name is not UNSET:
        db_item.name = new_name
    if new_description is not UNSET:
        db_item.description = new_description

    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    """
    Deletes an item and all its associated scans from the database.
    Returns True if deletion was successful, False if the item wasn't found.
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        return False

    db.delete(db_item)
    db.commit()
    return True


# ==========================================
# SCAN OPERATIONS
# ==========================================

def create_scan(db: Session, source: str, item_id: int, token: str | None = None):
    """
    Registers a unique physical scan event.
    Directly links the scan event to its corresponding Item ID.
    Supports optional token values (can be None).
    """
    db_scan = models.Scan(
        source=source,
        date=datetime.utcnow(),  # Auto-set server side timestamp
        token=token,
        item_id=item_id
    )
    db.add(db_scan)
    db.commit()
    db.refresh(db_scan)
    return db_scan


def get_scans(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of scan events along with their parent Item data.
    """
    return (
        db.query(models.Scan)
        .options(selectinload(models.Scan.item))
        .order_by(models.Scan.id.desc())  # Newest scans first
        .offset(skip)
        .limit(limit)
        .all()
    )

#Delete scan
def delete_scan(db: Session, scan_id: int):
    """
    Deletes a specific scan event from the database.
    Returns True if deletion was successful, False if the scan wasn't found.
    """
    db_scan = db.query(models.Scan).filter(models.Scan.id == scan_id).first()
    if not db_scan:
        return False

    db.delete(db_scan)
    db.commit()
    return True
