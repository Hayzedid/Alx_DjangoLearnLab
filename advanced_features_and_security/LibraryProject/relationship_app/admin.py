from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Book, Library, Librarian, UserProfile, CustomUser


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
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
