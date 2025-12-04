# Django Blog Project - Complete Documentation

## Project Overview

A comprehensive Django blogging platform with user authentication, blog post management, commenting system, tagging, and search functionality. Built with Django 5.2.6, Bootstrap 5, and django-taggit.

## Project Structure

```
django_blog/
├── django_blog/              # Project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
├── blog/                     # Blog application
│   ├── models.py            # Post and Comment models
│   ├── views.py             # All views (CRUD, auth, search)
│   ├── forms.py             # Forms for posts, comments, auth
│   ├── urls.py              # Blog URL patterns
│   ├── admin.py             # Admin configuration
│   ├── migrations/          # Database migrations
│   └── templates/blog/      # Blog templates
├── templates/               # Base templates
│   └── base.html           # Base template
├── static/                  # Static files (CSS, JS, images)
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
└── requirements.txt        # Python dependencies
```

## Installation & Setup

### 1. Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Access the blog at: `http://127.0.0.1:8000/`
Admin panel: `http://127.0.0.1:8000/admin/`

## Models

### Post Model
```python
- title: CharField(max_length=200)
- content: TextField()
- author: ForeignKey(User)
- published_date: DateTimeField(auto_now_add=True)
- updated_date: DateTimeField(auto_now=True)
- status: CharField (draft/published)
- tags: TaggableManager()
```

### Comment Model
```python
- post: ForeignKey(Post)
- author: ForeignKey(User)
- content: TextField()
- created_at: DateTimeField(auto_now_add=True)
- updated_at: DateTimeField(auto_now=True)
```

## Features Implemented

### ✅ Task 0: Initial Setup and Project Configuration
- [x] Django project created (`django_blog`)
- [x] Blog app created and registered
- [x] Database configured (SQLite)
- [x] Post model defined with all required fields
- [x] Migrations created and applied
- [x] Static files and templates directories configured
- [x] Development server tested

### ✅ Task 1: User Authentication System
- [x] User registration with extended form (email, first_name, last_name)
- [x] Login/Logout functionality
- [x] User profile management
- [x] Profile editing (email, first_name, last_name)
- [x] CSRF protection on all forms
- [x] Secure password handling
- [x] Authentication templates (login, register, profile)

### ✅ Task 2: Blog Post Management (CRUD)
- [x] ListView - Display all published posts
- [x] DetailView - Show individual posts
- [x] CreateView - Create new posts (authenticated users only)
- [x] UpdateView - Edit posts (author only)
- [x] DeleteView - Delete posts (author only)
- [x] Post status management (draft/published)
- [x] Proper permission checks
- [x] Templates for all operations

### ✅ Task 3: Comment Functionality
- [x] Comment model with post and author relationships
- [x] Display comments on post detail page
- [x] Create comments (authenticated users only)
- [x] Edit comments (comment author only)
- [x] Delete comments (comment author only)
- [x] Comment timestamps (created_at, updated_at)
- [x] Comment templates

### ✅ Task 4: Advanced Features (Tagging & Search)
- [x] Tag model integration (django-taggit)
- [x] Many-to-many relationship between Post and Tag
- [x] Tag management in post creation/editing
- [x] Tag filtering view (posts by tag)
- [x] Search functionality (title, content, tags)
- [x] Search results page
- [x] User posts view (posts by specific author)

## URL Patterns

```
Home:
  /                           - HomeView (latest posts)

Authentication:
  /register/                  - User registration
  /login/                     - User login
  /logout/                    - User logout
  /profile/                   - User profile

Blog Posts:
  /posts/                     - List all posts
  /posts/new/                 - Create new post
  /posts/<id>/                - Post detail
  /posts/<id>/edit/           - Edit post
  /posts/<id>/delete/         - Delete post

Comments:
  /posts/<id>/comments/new/   - Create comment
  /comments/<id>/edit/        - Edit comment
  /comments/<id>/delete/      - Delete comment

Tags & Search:
  /tags/<tag_name>/           - Posts by tag
  /search/                    - Search posts
  /author/<username>/         - Posts by author
```

## Views Overview

### Home & List Views
- **HomeView**: Display latest published posts with pagination
- **PostListView**: List all published posts
- **TagPostListView**: Filter posts by tag
- **SearchPostView**: Search posts by title, content, or tags
- **UserPostsView**: Display posts by specific author

### Authentication Views
- **RegisterView**: User registration with validation
- **CustomLoginView**: User login
- **CustomLogoutView**: User logout
- **ProfileView**: User profile display and editing

### Post Management Views
- **PostDetailView**: Display single post with comments
- **PostCreateView**: Create new post (LoginRequired)
- **PostUpdateView**: Edit post (Author only)
- **PostDeleteView**: Delete post (Author only)

### Comment Views
- **CommentCreateView**: Add comment to post (LoginRequired)
- **CommentUpdateView**: Edit comment (Author only)
- **CommentDeleteView**: Delete comment (Author only)

## Forms

### UserRegistrationForm
- Extends UserCreationForm
- Fields: username, email, first_name, last_name, password1, password2
- Email uniqueness validation

### UserProfileForm
- Fields: first_name, last_name, email
- Used for profile editing

### PostForm
- Fields: title, content, status, tags
- Bootstrap styling
- Tag input with comma separation

### CommentForm
- Fields: content
- Bootstrap textarea styling

### SearchForm
- Fields: query
- Used for search functionality

## Templates

### Base Template (`base.html`)
- Navigation bar with responsive menu
- Message display system
- Footer with links
- Bootstrap 5 styling
- Font Awesome icons

### Authentication Templates
- `login.html` - Login form
- `register.html` - Registration form
- `profile.html` - User profile and editing

### Blog Templates
- `home.html` - Homepage with latest posts
- `post_list.html` - All posts listing
- `post_detail.html` - Single post with comments
- `post_form.html` - Create/Edit post form
- `post_confirm_delete.html` - Delete confirmation

### Comment Templates
- `comment_form.html` - Create/Edit comment
- `comment_confirm_delete.html` - Delete confirmation

### Search & Tag Templates
- `search_results.html` - Search results
- `tag_posts.html` - Posts by tag
- `user_posts.html` - Posts by author

## Security Features

- ✅ CSRF protection on all forms
- ✅ Password hashing using Django's authentication
- ✅ LoginRequiredMixin for protected views
- ✅ UserPassesTestMixin for permission checks
- ✅ User ownership verification for edit/delete
- ✅ Email uniqueness validation
- ✅ SQL injection prevention (ORM usage)

## Styling

- Bootstrap 5 for responsive design
- Custom CSS for blog-specific styling
- Font Awesome icons
- Gradient backgrounds
- Card-based layout
- Mobile-friendly navigation

## Testing the Application

### User Registration
1. Go to `/register/`
2. Fill in username, email, password
3. Submit form
4. Redirect to login page

### Create a Post
1. Login to your account
2. Click "New Post"
3. Fill in title, content, select status
4. Add tags (comma-separated)
5. Submit

### Add Comments
1. View a post
2. Scroll to comments section
3. Fill in comment form
4. Submit

### Search Posts
1. Use search bar on homepage
2. Enter search query
3. View filtered results

### Filter by Tag
1. Click on any tag
2. View all posts with that tag

### View Author Posts
1. Click on author name
2. View all posts by that author

## Database Queries

### Get all published posts
```python
Post.objects.filter(status='published').order_by('-published_date')
```

### Get posts by tag
```python
Post.objects.filter(tags__name='django')
```

### Search posts
```python
from django.db.models import Q
Post.objects.filter(
    Q(title__icontains='search') |
    Q(content__icontains='search') |
    Q(tags__name__icontains='search')
).distinct()
```

### Get user's posts
```python
user.posts.filter(status='published')
```

### Get post comments
```python
post.comments.all()
```

## Admin Interface

Access admin at `/admin/` with superuser credentials.

### Post Admin
- List display: title, author, status, published_date
- Filters: status, published_date, author
- Search: title, content
- Fieldsets: Post Information, Tags, Dates

### Comment Admin
- List display: author, post, created_at
- Filters: created_at, author
- Search: content, author, post
- Fieldsets: Comment Information, Dates

## Deployment Checklist

- [ ] Set DEBUG = False in settings.py
- [ ] Update ALLOWED_HOSTS with domain
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up environment variables
- [ ] Configure static files collection
- [ ] Set up email backend
- [ ] Enable HTTPS
- [ ] Configure CSRF and CORS settings
- [ ] Set up database backups
- [ ] Configure logging
- [ ] Use production WSGI server (Gunicorn, uWSGI)

## Common Issues & Solutions

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic`

### Issue: Migrations not applying
**Solution**: 
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: Template not found
**Solution**: Ensure templates directory is in TEMPLATES['DIRS']

### Issue: Tags not working
**Solution**: Ensure django-taggit is installed and in INSTALLED_APPS

## Future Enhancements

- [ ] Email notifications for comments
- [ ] Post categories
- [ ] Like/favorite system
- [ ] User follow system
- [ ] Draft auto-save
- [ ] Rich text editor (TinyMCE, CKEditor)
- [ ] Image upload for posts
- [ ] Social sharing buttons
- [ ] Comment moderation
- [ ] User roles and permissions
- [ ] API endpoints (Django REST Framework)
- [ ] Pagination improvements
- [ ] Advanced search filters
- [ ] Post scheduling
- [ ] Analytics dashboard

## Dependencies

```
Django==5.2.6
django-taggit==6.1.0
Pillow==10.0.0
```

## File Structure Summary

| File | Purpose |
|------|---------|
| models.py | Post and Comment models |
| views.py | All view classes (CRUD, auth, search) |
| forms.py | User, Post, Comment forms |
| urls.py | URL routing |
| admin.py | Admin interface configuration |
| base.html | Base template with navigation |
| home.html | Homepage |
| post_detail.html | Single post with comments |
| login.html | Login form |
| register.html | Registration form |

## Support & Documentation

- Django Documentation: https://docs.djangoproject.com/
- django-taggit: https://django-taggit.readthedocs.io/
- Bootstrap: https://getbootstrap.com/
- Font Awesome: https://fontawesome.com/

## License

This project is open source and available under the MIT License.

## Author

Created as part of the Alx Django Learning Lab project.

---

**Status**: ✅ All Tasks Completed  
**Last Updated**: December 2025  
**Version**: 1.0
