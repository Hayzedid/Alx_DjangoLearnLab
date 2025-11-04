# Update Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
```

## Expected Output
```
Updated title: Nineteen Eighty-Four
```

## Description
This command retrieves the book with title "1984", updates its title to "Nineteen Eighty-Four", and saves the changes to the database.
