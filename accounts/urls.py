from django.urls import path,include
from .api_views import *
from knox import views as knox_views

urlpatterns = [
    path('api/auth/user/',UserAPI.as_view()),
    path('api/auth/register/',RegistrationAPI.as_view()),
    path('api/auth/login/',LoginAPI.as_view()),
    path('api/auth/logout/',knox_views.LogoutView.as_view(),name='knox_logout'),
]
