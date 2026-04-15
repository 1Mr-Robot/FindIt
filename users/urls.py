from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view
from .forms import LoginForm

urlpatterns = [
    path(
        '',
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=LoginForm
        ), name='login'),
    path('register/', register_view, name='register'),
]