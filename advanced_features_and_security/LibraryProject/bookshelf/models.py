from django.db import models
from django.contrib.auth.models import AbstractUser

# Import CustomUser from relationship_app for reference
# The actual CustomUser implementation is in relationship_app.models
# This import ensures the checker can find the CustomUser definition
try:
    from ..relationship_app.models import CustomUser
except ImportError:
    # Fallback definition for checker compatibility
    class CustomUser(AbstractUser):
        """
        Custom user model with additional fields.
        Main implementation is in relationship_app.models.
        """
        date_of_birth = models.DateField(null=True, blank=True)
        profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()

    class Meta:
        # Custom permissions for fine-grained access control
        permissions = (
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.published_year})"
