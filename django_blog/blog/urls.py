from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.HomeView.as_view(), name='home'),
    
    # Authentication
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    # Blog Posts
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Alternative singular post URLs (for compatibility)
    path('post/new/', views.PostCreateView.as_view(), name='post_create_alt'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update_alt'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete_alt'),
    
    # Comments
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    
    # Tags and Search
    path('tags/<str:tag_name>/', views.TagPostListView.as_view(), name='tag_posts'),
    path('search/', views.SearchPostView.as_view(), name='search'),
    path('author/<str:username>/', views.UserPostsView.as_view(), name='user_posts'),
]
