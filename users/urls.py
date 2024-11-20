from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/<int:pk>/', views.ProdileDeleteView.as_view(), name='profile'),
    path('logout/', views.user_logout, name='logout')
]
