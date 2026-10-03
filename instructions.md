# Library Search

**Module:** 5 — FastAPI Development
**Estimated time:** 35 minutes

## Objective

Build a library catalog API that demonstrates the difference between path parameters and query parameters. Implement search, filtering, and sorting using query parameters with validation constraints.

## What You'll Do

1. In `app/schemas/book.py`, define:
   - A `SortField` enum with values: title, author, rating, year.
   - A `Book` schema with fields: id, title, author, genre, rating (0-5), year, available.
2. In `app/routers/books.py`:
   - Populate the `BOOKS` list with at least 10 books across multiple genres.
   - Implement `GET /{book_id}` — return a single book by path parameter, or 404.
   - Implement `GET /` — search and filter books using query parameters (genre, min_rating, sort_by, limit) with `Query()` constraints.
   - Implement `GET /authors/{author_id}/books` — return all books by a given author.
3. In `app/main.py`, import and include the books router with `prefix="/books"`.

## Starter Code

```
app/
  __init__.py
  main.py              — FastAPI app; needs router inclusion
  schemas/
    __init__.py
    book.py            — Schema stubs for SortField enum and Book model
  routers/
    __init__.py
    books.py           — Endpoint stubs with empty BOOKS list
```

## Running

```bash
uvicorn app.main:app --reload
```

## Deliverable

A searchable library API where users can filter by genre, set a minimum rating, sort by different fields, and limit results -- all via query parameters visible in the Swagger docs.
