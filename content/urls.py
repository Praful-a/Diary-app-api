from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.loginpage, name='login'),
    path("logout/", views.logoutpage, name='logout'),
    path('home/', views.diary, name='home'),
    path('add/', views.add, name='add'),
    path('<slug>/edit', views.edit, name='edit'),
    path('<slug>/delete', views.delete, name='delete'),
    path('must_authenticate/', views.must_authenticate, name='must_authenticate')
]
