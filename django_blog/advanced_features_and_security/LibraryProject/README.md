# LibraryProject - Advanced Features and Security

This Django project demonstrates advanced features including custom user models, permissions management, and comprehensive security implementations.

## Features Implemented

### 1. Custom User Model
- **CustomUser**: Extends `AbstractUser` with additional fields:
  - `date_of_birth`: DateField for user's birth date
  - `profile_photo`: ImageField for user profile pictures
- **CustomUserManager**: Handles user creation with custom fields
- **Admin Integration**: Full admin interface support for custom user management

### 2. Permissions and Groups System
- **Custom Permissions**: `can_view`, `can_create`, `can_edit`, `can_delete` on Book model
- **Permission-Protected Views**: All CRUD views use `@permission_required` decorators with `raise_exception=True`
- **Groups Setup**: Viewers, Editors, and Admins groups with appropriate permissions

### 3. Security Best Practices
- **HTTPS Enforcement**: `SECURE_SSL_REDIRECT = True`
- **HSTS Configuration**: 1-year HSTS policy with subdomains and preload
- **Secure Cookies**: Session and CSRF cookies only over HTTPS
- **Security Headers**: XSS protection, content type nosniff, frame options
- **CSRF Protection**: All forms include `{% csrf_token %}`
- **CSP Middleware**: Custom Content Security Policy implementation

### 4. Form Handling
- **ExampleForm**: ModelForm for Book creation with validation
- **Secure Views**: All views use Django ORM and form validation
- **Template Security**: CSRF tokens in all forms

## Project Structure

```
LibraryProject/
├── LibraryProject/          # Django project settings
│   ├── settings.py          # Security configurations
│   ├── middleware.py        # CSP middleware
│   └── ...
├── bookshelf/               # Book management app
│   ├── models.py            # Book model with permissions
│   ├── forms.py             # ExampleForm
│   ├── views.py             # Permission-protected views
│   └── templates/           # HTML templates
├── relationship_app/        # User management app
│   ├── models.py            # CustomUser and CustomUserManager
│   ├── admin.py             # CustomUserAdmin
│   └── ...
└── README.md               # This file
```

## Security Settings

All security settings are configured in `LibraryProject/settings.py`:

- `SECURE_SSL_REDIRECT = True`
- `SECURE_HSTS_SECONDS = 31536000`
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
- `SECURE_HSTS_PRELOAD = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`
- `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')`

## Usage

1. Run migrations: `python manage.py migrate`
2. Create superuser: `python manage.py createsuperuser`
3. Start server: `python manage.py runserver`
4. Access admin at `/admin/` to manage users and permissions

## Testing Permissions

1. Create groups in Django Admin: Viewers, Editors, Admins
2. Assign permissions to groups
3. Create test users and assign to groups
4. Test access to protected views

This implementation demonstrates Django best practices for security, user management, and permissions handling.
