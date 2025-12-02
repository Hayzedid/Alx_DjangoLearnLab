# Delete Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Confirm deletion
all_books = Book.objects.all()
print(f"Total books remaining: {all_books.count()}")
```

## Expected Output
```
Book deleted successfully
Total books remaining: 0
```

## Description
This command retrieves the book with title "Nineteen Eighty-Four", deletes it from the database, and confirms the deletion by checking that no books remain in the database.
