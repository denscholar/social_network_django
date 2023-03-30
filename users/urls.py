from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homePage, name='home_page'),
    path("login/", views.loginView, name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path("password_change_done/", auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]
