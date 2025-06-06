#define URL route for index() view
from django.urls import path
from . import views

app_name = 'restaurante'  # Define the app namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name = 'menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
