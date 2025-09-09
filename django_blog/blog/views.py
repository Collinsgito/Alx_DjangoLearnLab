from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView, LogoutView

from .models import Post
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, PostForm


# ---------------------------
# Authentication Views
# ---------------------------

def register(request):
    """User registration view."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the new user
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    """Custom login using templates/registration/login.html"""
    template_name = 'blog/login.html'


class CustomLogoutView(LogoutView):
    """Custom logout confirmation"""
    template_name = 'blog/logged_out.html'


@login_required
def profile_view(request):
    """Show logged-in user profile"""
    return render(request, 'registration/profile.html')


@login_required
def profile_edit(request):
    """Edit user & profile info"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=getattr(request.user, "profile", None)  # safe check
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(
            instance=getattr(request.user, "profile", None)
        )

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'registration/profile_edit.html', context)


# ---------------------------
# Blog Post Views (CRUD)
# ---------------------------

class PostListView(ListView):
    """List all posts"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    """View a single post"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create a new post (auth required)"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit an existing post (only by author)"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a post (only by author)"""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
