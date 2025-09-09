from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally login user immediately
            login(request, user)
            return redirect('post_list')   # or 'profile' 
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form': form})

from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'blog/logged_out.html'  # optional simple confirmation

@login_required
def profile_view(request):
    # show profile
    return render(request, 'blog/profile.html', {})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'blog/profile_edit.html', context)