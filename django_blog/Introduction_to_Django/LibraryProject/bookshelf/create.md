# Create Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created book: {book}")
```

## Expected Output
```
Created book: 1984
```

## Description
This command creates a new Book instance with the title "1984", author "George Orwell", and publication year 1949. The book is automatically saved to the database using the `create()` method.
