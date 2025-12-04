from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    Example form for demonstrating form handling and CSRF protection.
    This form is used to create and edit Book instances.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'published_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter publication year'}),
        }

    def clean_published_year(self):
        """
        Custom validation for published_year field.
        Ensures the year is reasonable (not in the future or too far in the past).
        """
        year = self.cleaned_data.get('published_year')
        if year:
            from datetime import datetime
            current_year = datetime.now().year
            if year > current_year:
                raise forms.ValidationError("Publication year cannot be in the future.")
            if year < 1000:
                raise forms.ValidationError("Publication year seems too old.")
        return year
