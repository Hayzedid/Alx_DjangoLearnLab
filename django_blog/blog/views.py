from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Post, Comment
from .forms import (
    UserRegistrationForm, UserProfileForm, PostForm, 
    CommentForm, SearchForm
)


# ============ HOME VIEW ============

class HomeView(ListView):
    """Display all published blog posts"""
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-published_date')


# ============ AUTHENTICATION VIEWS ============

class RegisterView(View):
    """User registration view"""
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'blog/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        return render(request, 'blog/register.html', {'form': form})


class CustomLoginView(LoginView):
    """Custom login view"""
    template_name = 'blog/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    """Custom logout view"""
    next_page = 'home'


class ProfileView(LoginRequiredMixin, View):
    """User profile view"""
    login_url = 'login'
    
    def get(self, request):
        form = UserProfileForm(instance=request.user)
        posts = request.user.posts.all()
        context = {
            'form': form,
            'posts': posts,
            'user_obj': request.user
        }
        return render(request, 'blog/profile.html', context)
    
    def post(self, request):
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        posts = request.user.posts.all()
        context = {
            'form': form,
            'posts': posts,
            'user_obj': request.user
        }
        return render(request, 'blog/profile.html', context)


# ============ BLOG POST VIEWS ============

class PostListView(ListView):
    """Display all published blog posts with pagination"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-published_date')


class PostDetailView(DetailView):
    """Display a single blog post with comments"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create a new blog post"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update a blog post"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a blog post"""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)


# ============ COMMENT VIEWS ============

class CommentCreateView(LoginRequiredMixin, CreateView):
    """Create a new comment on a post"""
    model = Comment
    form_class = CommentForm
    login_url = 'login'
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.author = self.request.user
        form.instance.post = post
        messages.success(self.request, 'Comment posted successfully!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update a comment"""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    login_url = 'login'
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def form_valid(self, form):
        messages.success(self.request, 'Comment updated successfully!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a comment"""
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    login_url = 'login'
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Comment deleted successfully!')
        return super().delete(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})


# ============ TAG AND SEARCH VIEWS ============

class TagPostListView(ListView):
    """Display all posts with a specific tag"""
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Post.objects.filter(
            status='published',
            tags__name=tag_name
        ).distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_name']
        return context


class SearchPostView(ListView):
    """Search for blog posts"""
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Post.objects.filter(
                status='published'
            ).filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.filter(status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class UserPostsView(ListView):
    """Display all posts by a specific user"""
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.posts.filter(status='published').order_by('-published_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_object_or_404(User, username=self.kwargs['username'])
        return context


# Alias for TagPostListView (for compatibility)
class PostByTagListView(TagPostListView):
    """Alias for TagPostListView - Display all posts with a specific tag"""
    pass

