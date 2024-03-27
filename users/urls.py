from django.urls import path
from .views import RegisterView, LoginView, logout_user, ProfileView, Profile

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',logout_user , name='logout'),
    path('profile/',ProfileView.as_view() , name='profile'),
    path('profileview/',Profile.as_view() , name='profile_view'),
]
