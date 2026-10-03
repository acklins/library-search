# L4 — Library Search endpoints

from fastapi import APIRouter, Query, HTTPException
from app.schemas.book import Book, SortField
from typing import Optional

router = APIRouter()

# Sample in-memory library — 12 books across multiple genres
BOOKS: list[dict] = [
    {
        "id": 1,
        "title": "Becoming", 
        "author": "Michelle Obama", 
        "genre": "Memoir", 
        "rating": 5.0, 
        "year": 2018,
        "available": True
    },
    {   "id": 2,
        "title": "The Audacity of Hope", 
        "author": "Barack Obama", 
        "genre": "Memoir", 
        "rating": 5.0, 
        "year": 2006,
        "available": True
    },
    {
        "id": 3,
        "title": "A Promised Land, Dreams from My Father", 
        "author": "Barack Obama", 
        "genre": "Memoir", 
        "rating": 5.0, 
        "year": 1995,
        "available": False
    },
    {   "id": 4,
        "title": "Black Cake", 
        "author": "Charmaine Wilkerson", 
        "genre": "Literary fiction", 
        "rating": 4.5, 
        "year": 2022,
        "available": True
    },
    {
        "id": 5,
        "title": "Kofi and His Magic",
        "author": "Maya Angelou", 
        "genre": "Children's Literature", 
        "rating": 4.0, 
        "year": 1994,
        "available": True
    },
    {
        "id": 6,
        "title": "The Survival of the Thickest",
        "author": "Michelle Buteau", 
        "genre": "Memoir", 
        "rating": 4.6, 
        "year": 2020,
        "available": True
    },
    {
        "id": 7,
        "title": "Sugar Plum Ballerinas", 
        "author": "Whoopi Goldberg", 
        "genre": "Children's Fiction", 
        "rating": 4.7, 
        "year": 2008,
        "available": True
    },
    {   "id": 8,
        "title": "Food, Health and Happiness", 
        "author": "Oprah Winfrey", 
        "genre": "Cookbook", 
        "rating": 4.9, 
        "year": 2017,
        "available": True
    },
    {
        "id": 9,
        "title": "Born A Crime", 
        "author": "Trevor Noah", 
        "genre": "Memoir", 
        "rating": 5.0, 
        "year": 2016,
        "available": True
    },
    {
        "id": 10,
        "title": "The Last Black Unicorn", 
        "author": "Tiffany Haddish", 
        "genre": "Biography", 
        "rating": 4.3, 
        "year": 2017,
        "available": True
    },
    {   "id": 11,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.6,
        "year": 1813,
        "available": False,
    },
    {
        "id": 12,
        "title": "Emma",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.2,
        "year": 1815,
        "available": True,
    },    
]
AUTHORS = {
    1: "Charmaine Wilkerson",
    2: "Jane Austen",
    3: "Maya Angelou",
    4: "Michelle Buteau",
    5: "Whoopi Goldberg",
    6: "Oprah Winfrey",
    7: "Trevor Noah",
    8: "Tiffany Haddish",
    9: "Michelle Obama",
    10: "Barack Obama",
}

# Return all books by a given author (use author_id as an index into a small
@router.get("/authors/{author_id}/books", response_model=list[Book])
def get_books_by_author(author_id: int):
    if author_id not in AUTHORS:
        raise HTTPException(
            status_code=404, 
            detail="Author not found"
        )
    author_name = AUTHORS[author_id]
    
    return [
        book 
        for book in BOOKS 
        if book["author"] == author_name
    ]

#Search books
@router.get("/", response_model=list[Book])
def search_books(
    genre: Optional[str] = Query(None, description="Filter by genre"),
    min_rating: float = Query(
        0.0, 
        ge=0.0, 
        le=5.0, 
        description="Minimum rating"
    ),
    sort_by: SortField = Query(
        SortField.title, 
        description="Sort field"
    ),
    limit: int = Query(
        10, 
        ge=1, 
        le=100, 
        description="Max results to return"
    ),
):
#1st create a copy of the books list to avoid modifying the original
    results = BOOKS.copy()

    if genre:
        results = [
            book 
            for book in results 
            if book["genre"].lower() == genre.lower()
        ]

    results = [
        book 
        for book in results 
        if book["rating"] >= min_rating
    ]
    #sort the books
    results.sort(
        key=lambda book: book[sort_by.value]
    )

    return results[:limit]

#Returns a single book by ID
@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
        
    raise HTTPException(
        status_code=404, 
        detail="Book not found"
    )




