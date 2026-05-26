from pydantic import BaseModel
from datetime import datetime

# Base schemas without relationships
class ItemBase(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None

    class Config:
        from_attributes = True

class ScanBase(BaseModel):
    id: int | None = None
    text: str
    source: str
    date: datetime | None = None

    class Config:
        from_attributes = True

class TokenBase(BaseModel):
    id: int | None = None
    text: str
    source: str
    date: datetime | None = None
    item_id: int | None = None
    scan_id: int | None = None

    class Config:
        from_attributes = True

# Nested schemas for relationships
class TokenWithRelations(BaseModel):
    id: int
    text: str
    source: str
    date: datetime | None = None
    item_id: int | None = None
    scan_id: int | None = None
    item: ItemBase | None = None
    scan: ScanBase | None = None

    class Config:
        from_attributes = True

class ItemWithTokens(BaseModel):
    id: int
    name: str
    description: str | None = None
    tokens: list[TokenWithRelations] = []

    class Config:
        from_attributes = True

class ScanWithTokens(BaseModel):
    id: int
    text: str
    source: str
    date: datetime | None = None
    tokens: list[TokenWithRelations] = []

    class Config:
        from_attributes = True

# Keep simple versions for backward compatibility
class Item(ItemBase):
    pass

class Scan(ScanBase):
    pass

class Token(TokenBase):
    pass
