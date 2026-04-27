from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view, register_view, profile_view, update_profile_view

urlpatterns = [
    path('', login_view.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', update_profile_view, name='update_profile'),
]