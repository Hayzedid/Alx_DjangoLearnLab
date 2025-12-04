# CRUD Operations Documentation

This document contains all the CRUD (Create, Read, Update, Delete) operations performed on the Book model using Django's ORM through the Django shell.

## Setup
First, open the Django shell:
```bash
python manage.py shell
```

## 1. Create Operation

### Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created book: {book}")
```

### Output:
```
Created book: 1984
```

### Description:
Creates a new Book instance with the specified attributes and saves it to the database.

---

## 2. Retrieve Operation

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

### Output:
```
Title: 1984
Author: George Orwell
Publication Year: 1949
```

### Description:
Retrieves the book with title "1984" and displays all its attributes.

---

## 3. Update Operation

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
```

### Output:
```
Updated title: Nineteen Eighty-Four
```

### Description:
Updates the title of the book from "1984" to "Nineteen Eighty-Four" and saves the changes.

---

## 4. Delete Operation

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Confirm deletion
all_books = Book.objects.all()
print(f"Total books remaining: {all_books.count()}")
```

### Output:
```
Book deleted successfully
Total books remaining: 0
```

### Description:
Deletes the book from the database and confirms the deletion by checking the total count of remaining books.

---

## Model Definition

The Book model is defined in `bookshelf/models.py` with the following structure:

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
```

## Database Migration

The model was migrated to the database using:
```bash
python manage.py makemigrations bookshelf
python manage.py migrate
```
