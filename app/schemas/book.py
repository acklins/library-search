# L4 — Library Search — Book schema and sort enum

from pydantic import BaseModel, Field
from enum import Enum

#Four valid sorting choices
class SortField(str, Enum):
    title = "title"
    author = "author"
    rating = "rating"
    year = "year"

#Represents a book in the library catalog.
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    rating: float = Field(ge=0.0, le=5.0)
    year: int
    available: bool
