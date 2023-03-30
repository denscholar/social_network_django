from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def loginView(request):
    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data=data)
        if form.is_valid():
            # clean the data first
            data = form.cleaned_data
            # authenticate the user
            user = authenticate(request, username=data['username'], password=data['password'])
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
    return render(request, "users/index.html")