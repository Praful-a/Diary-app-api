from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, 'login')
router.register('feed', views.UserDataViewSet)

urlpatterns = [
    path('', include(router.urls))
]
