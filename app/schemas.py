from pydantic import BaseModel

class Item(BaseModel):
    items: str
    scans: str
    tokens: str
    date: str

class Scan(BaseModel):
    text: str
    source: str

class Token(BaseModel):
    text: str
    source: str
    date: str

