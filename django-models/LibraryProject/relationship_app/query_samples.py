"""
Sample queries demonstrating relationships in relationship_app.
Run this file with Django context, e.g.:

    python manage.py shell -c "exec(open('relationship_app/query_samples.py').read())"

Or run as a script after setting DJANGO_SETTINGS_MODULE and calling django.setup().
"""
import os
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
    django.setup()

    from relationship_app.models import Author, Book, Library, Librarian

    # Query all books by a specific author
    author_name = 'Jane Doe'
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for b in books_by_author:
            print('-', b.title)
    except Author.DoesNotExist:
        print(f"No author named {author_name}")

    # List all books in a library
    library_name = 'Central Library'
    try:
        lib = Library.objects.get(name=library_name)
        print(f"Books in {library_name}:")
        for b in lib.books.all():
            print('-', b.title, 'by', b.author.name)
    except Library.DoesNotExist:
        print(f"No library named {library_name}")

    # Retrieve librarian for a library
    try:
        lib = Library.objects.get(name=library_name)
        if hasattr(lib, 'librarian'):
            print(f"Librarian for {library_name}: {lib.librarian.name}")
        else:
            print(f"No librarian assigned to {library_name}")
    except Library.DoesNotExist:
        pass
