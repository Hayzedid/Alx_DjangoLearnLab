from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .models import Book

# Create your views here.

@permission_required('LibraryProject.bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to display a list of all books.
    Demonstrates secure data access using Django ORM.
    Protected by can_view permission with raise_exception=True.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('LibraryProject.bookshelf.can_create', raise_exception=True)
def form_example(request):
    """
    Example view demonstrating form handling with CSRF protection.
    Uses ExampleForm to create new Book instances.
    Protected by can_create permission with raise_exception=True.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Form validation ensures secure data handling
            form.save()
            return render(request, 'bookshelf/form_example.html', {
                'form': ExampleForm(),  # Reset form after successful submission
                'success': True
            })
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})
