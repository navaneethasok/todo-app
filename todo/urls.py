from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('delete/<str:pk>/', views.delete, name='delete'),

    path('complete/<str:pk>/', views.complete, name='complete'),

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
]
