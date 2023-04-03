from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserEditForm, ProfileEditForm
from posts.models import Post


def loginView(request):
    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data=data)
        if form.is_valid():
            # clean the data first
            data = form.cleaned_data
            # authenticate the user
            user = authenticate(
                request, username=data['username'], password=data['password'])
            # check if the user is present
            if user is not None:
                login(request, user)
                return HttpResponse("User logged in")
            else:
                return HttpResponse("Invalid credentials")

    form = LoginForm()
    context = {
        "form": form
    }
    return render(request, 'users/login.html', context)


@login_required
def homePage(request):
    # get access to the currently logged in user
    current_user = request.user
    posts = Post.objects.filter(user=current_user)
    context = {
        "posts": posts
    }
    return render(request, "users/index.html", context)


def register(request):
    if request.method == 'POST':
        data = request.POST
        user_form = RegistrationForm(data=data)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # this creates a new user profile as soon a user registers
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
    else:
        user_form = RegistrationForm()

    return render(request, 'users/register.html', {"user_form": user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        data = request.POST
        user_form = UserEditForm(instance=request.user, data=data)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=data, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'users/edit_success.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

    return render(request, 'users/edit.html', context)
