# Advanced Features and Security - Django Project

This project demonstrates advanced Django features including custom user models, permissions management, and comprehensive security implementations.

## Project Structure

```
advanced_features_and_security/
├── LibraryProject/
│   ├── settings.py          # Main configuration with security settings
│   ├── middleware.py        # Custom CSP middleware
│   └── ...
├── bookshelf/               # App with Book model and permissions
├── relationship_app/        # Main app with custom user model
└── README.md               # This documentation
```

## 1. Custom User Model Implementation

### Features Implemented
- **CustomUser Model**: Extends `AbstractUser` with additional fields:
  - `date_of_birth`: DateField for user's birth date
  - `profile_photo`: ImageField for user profile pictures
- **CustomUserManager**: Handles user creation with custom fields
- **Admin Integration**: Full admin interface support for custom user management

### Key Files
- `relationship_app/models.py`: Contains `CustomUser` and `CustomUserManager`
- `relationship_app/admin.py`: Admin configuration for custom user
- `LibraryProject/settings.py`: `AUTH_USER_MODEL` configuration

### Usage
```python
# The custom user model is automatically used throughout the application
# Access custom fields:
user.date_of_birth
user.profile_photo
```

## 2. Permissions and Groups System

### Custom Permissions Defined
Both `relationship_app.Book` and `bookshelf.Book` models include:
- `can_view`: Permission to view books
- `can_create`: Permission to create new books
- `can_edit`: Permission to edit existing books
- `can_delete`: Permission to delete books

### Recommended Groups Setup
Create these groups in Django Admin and assign permissions:

#### Viewers Group
- Permissions: `can_view`
- Purpose: Read-only access to books

#### Editors Group
- Permissions: `can_view`, `can_create`, `can_edit`
- Purpose: Can manage books but not delete them

#### Admins Group
- Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
- Purpose: Full access to all book operations

### View Protection
Views are protected using `@permission_required` decorators:
```python
@permission_required('relationship_app.can_view', raise_exception=True)
def list_books(request):
    # View implementation
```

## 3. Security Best Practices Implementation

### Security Settings Configured

#### Development Settings (Current)
```python
DEBUG = True  # Set to False in production
SECURE_SSL_REDIRECT = False  # Set to True in production
SESSION_COOKIE_SECURE = False  # Set to True in production
CSRF_COOKIE_SECURE = False  # Set to True in production
```

#### Production-Ready Security Settings
```python
# Security headers and protections
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS and HSTS (configure for production)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### CSRF Protection
- All forms include `{% csrf_token %}` tags
- CSRF middleware is enabled in settings
- Templates: `login.html`, `register.html`, `book_form.html`

### Content Security Policy (CSP)
- Custom middleware: `LibraryProject/middleware.py`
- Policy: Restricts resource loading to same origin
- Prevents XSS attacks by controlling script and style sources

### SQL Injection Prevention
- All database queries use Django ORM
- User input validation through Django forms
- No raw SQL or string concatenation in queries

## 4. HTTPS and Secure Communication

### Current Configuration
The application is configured with development-friendly defaults but includes production-ready settings that can be activated.

### Production Deployment Checklist
1. **Update settings.py**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com']
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

2. **Web Server Configuration**:
   - Configure SSL/TLS certificates (e.g., Let's Encrypt)
   - Update Nginx/Apache configuration for HTTPS
   - Ensure proper certificate chain and security headers

3. **Security Headers**:
   - All security headers are configured in Django settings
   - CSP middleware provides additional XSS protection
   - HSTS headers enforce HTTPS usage

## 5. Setup and Testing Instructions

### Initial Setup
1. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

3. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

### Testing Permissions
1. **Access Django Admin** (`/admin/`)
2. **Create Groups**:
   - Navigate to Groups section
   - Create: Viewers, Editors, Admins
   - Assign appropriate permissions to each group

3. **Create Test Users**:
   - Create users with different group memberships
   - Test access to book operations based on permissions

4. **Verify Security**:
   - Check that forms include CSRF tokens
   - Verify CSP headers in browser developer tools
   - Test permission enforcement on protected views

### Manual Testing Scenarios
- **Viewer User**: Can access book list but cannot create/edit/delete
- **Editor User**: Can view, create, and edit books but cannot delete
- **Admin User**: Has full access to all book operations
- **Unauthenticated User**: Cannot access protected views

## 6. Security Measures Summary

### Implemented Protections
- **CSRF Protection**: All forms protected with CSRF tokens
- **XSS Prevention**: CSP headers and input validation
- **SQL Injection Prevention**: Django ORM usage throughout
- **Clickjacking Protection**: X-Frame-Options header set to DENY
- **Content Type Sniffing Protection**: SECURE_CONTENT_TYPE_NOSNIFF enabled
- **Custom User Model**: Enhanced user management with additional fields
- **Permission-Based Access Control**: Fine-grained permissions on models and views

### Production Considerations
- Enable HTTPS-only settings when deploying with SSL
- Configure proper ALLOWED_HOSTS for your domain
- Set up proper logging and monitoring
- Regular security updates and dependency management
- Consider additional security middleware for production environments

## 7. File Modifications Summary

### Core Files Modified
- `relationship_app/models.py`: Custom user model and permissions
- `relationship_app/admin.py`: Custom user admin interface
- `relationship_app/views.py`: Permission-protected views
- `bookshelf/models.py`: Added custom permissions
- `LibraryProject/settings.py`: Security and user model configuration
- `LibraryProject/middleware.py`: Custom CSP middleware

### Templates
All form templates include proper CSRF protection:
- `relationship_app/templates/relationship_app/login.html`
- `relationship_app/templates/relationship_app/register.html`
- `relationship_app/templates/relationship_app/book_form.html`

This implementation provides a robust foundation for a secure Django application with proper user management, permissions, and security best practices.
