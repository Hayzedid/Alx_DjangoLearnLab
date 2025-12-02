# Django Blog - Quick Start Guide

## 5-Minute Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py migrate
```

### Step 3: Create Admin User
```bash
python manage.py createsuperuser
```

### Step 4: Start Server
```bash
python manage.py runserver
```

### Step 5: Access the Blog
- **Blog**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

---

## Common Tasks

### Create a Blog Post
1. Login to your account
2. Click "New Post" in navigation
3. Fill in title and content
4. Add tags (comma-separated)
5. Select status (Draft/Published)
6. Click "Save"

### Register New User
1. Click "Register" link
2. Fill in username, email, password
3. Click "Register"
4. Login with new credentials

### Search Posts
1. Use search bar on homepage
2. Search by title, content, or tags
3. View results

### Filter by Tag
1. Click any tag on a post
2. View all posts with that tag

### Manage Your Profile
1. Click "Profile" in navigation
2. Edit your information
3. Click "Save"

---

## URL Quick Reference

| URL | Purpose |
|-----|---------|
| `/` | Homepage |
| `/register/` | Register new user |
| `/login/` | Login |
| `/logout/` | Logout |
| `/profile/` | Your profile |
| `/posts/` | All posts |
| `/posts/new/` | Create post |
| `/posts/<id>/` | View post |
| `/posts/<id>/edit/` | Edit post |
| `/posts/<id>/delete/` | Delete post |
| `/search/?q=keyword` | Search posts |
| `/tags/<tag-name>/` | Posts by tag |
| `/author/<username>/` | Posts by author |
| `/admin/` | Admin panel |

---

## Admin Panel Features

### Manage Posts
- View all posts
- Filter by status, date, author
- Search posts
- Edit/delete posts

### Manage Comments
- View all comments
- Filter by date, author
- Search comments
- Delete comments

---

## Tips & Tricks

### Markdown in Posts
Use markdown syntax in post content:
```
# Heading
**Bold text**
*Italic text*
- List item
```

### Tag Management
- Add multiple tags: `python, django, web`
- Tags are case-sensitive
- Click tags to filter

### Search Operators
- Search by title: `title:keyword`
- Search by author: `author:username`
- Search by tag: `tag:tagname`

---

## Troubleshooting

### Issue: "No such table" error
**Solution**: Run `python manage.py migrate`

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic`

### Issue: Can't login
**Solution**: Check username/password, or create new superuser

### Issue: Tags not working
**Solution**: Ensure django-taggit is installed: `pip install django-taggit`

---

## Development Commands

```bash
# Create new app
python manage.py startapp appname

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Access Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

---

## File Locations

- **Models**: `blog/models.py`
- **Views**: `blog/views.py`
- **Forms**: `blog/forms.py`
- **URLs**: `blog/urls.py`
- **Templates**: `templates/blog/`
- **Static**: `static/`
- **Database**: `db.sqlite3`

---

## Next Steps

1. Customize the blog design in `templates/base.html`
2. Add more fields to Post model
3. Implement email notifications
4. Add user profiles with avatars
5. Deploy to production

---

## Support

For issues or questions:
1. Check `DJANGO_BLOG_README.md` for detailed documentation
2. Review Django documentation: https://docs.djangoproject.com/
3. Check django-taggit docs: https://django-taggit.readthedocs.io/

---

**Happy Blogging! 🚀**
