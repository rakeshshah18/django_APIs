from django.urls import path
from .views import MenuItemView, MenuItemDetailView

urlpatterns = [
    path('menu-items/', MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view()),
    
]