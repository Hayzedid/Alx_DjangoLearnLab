from django.contrib import admin
from .models import Book


# Define the custom configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    # 1. Display title, author, and published_year in the list view (columns)
    list_display = ('title', 'author', 'published_year')

    # 2. Add filters on the right sidebar (for easy filtering)
    list_filter = ('author', 'published_year')

    # 3. Add a search bar that searches the specified fields
    search_fields = ('title', 'author')

# Register your models here.
admin.site.register(Book, BookAdmin)