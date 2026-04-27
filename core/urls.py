from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item_found/<int:item_id>/', views.item_found, name='item_found'),
    path('report_object/', views.report_object, name='report_object'),
]