from django.urls import path
from .views import login_view, register_view

urlpatterns = [
    path('', login_view.as_view(), name='login'),
    path('register/', register_view, name='register'),
]