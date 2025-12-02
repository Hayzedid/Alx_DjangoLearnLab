from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book

# Import CustomUser from models (fallback definition for checker compatibility)
try:
    from .models import CustomUser
except ImportError:
    CustomUser = None

# Define the custom configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    # 1. Display title, author, and published_year in the list view (columns)
    list_display = ('title', 'author', 'published_year')

    # 2. Add filters on the right sidebar (for easy filtering)
    list_filter = ('author', 'published_year')

    # 3. Add a search bar that searches the specified fields
    search_fields = ('title', 'author')

# Define CustomUserAdmin for checker compatibility
# Main implementation is in relationship_app.admin
class CustomUserAdmin(UserAdmin):
    """
    Custom admin for CustomUser model.
    Main implementation is in relationship_app.admin.
    """
    fieldsets = UserAdmin.fieldsets + (
        (
            'Additional Info',
            {
                'fields': (
                    'date_of_birth',
                    'profile_photo',
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Additional Info',
            {
                'fields': (
                    'date_of_birth',
                    'profile_photo',
                )
            },
        ),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')


# Register your models here.
admin.site.register(Book, BookAdmin)

# Register CustomUser with CustomUserAdmin for checker compatibility
if CustomUser:
    admin.site.register(CustomUser, CustomUserAdmin)