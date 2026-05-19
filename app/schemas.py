from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description:  str | None = None

class Scan(BaseModel):
    text: str
    source: str

class Token(BaseModel):
    text: str
    source: str
    date: str
    item_id: int | None = None
    scan_id: int | None = None
