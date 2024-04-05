from django.urls import path
from .views import (RegisterView, LoginView,
                    logout_user, ProfileView,
                    Profile,UsersViews,SendFriendRequest,
                    MyNetworksView,AddFriendRequest,DeleteFriend,IgnoreFriendRequest,ResetPasswordView)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',logout_user , name='logout'),
    path('profile/',ProfileView.as_view() , name='profile'),
    path('reset-password/',ResetPasswordView.as_view() , name='reset_password'),
    path('profile-view/',Profile.as_view() , name='profile_view'),
    path('list/',UsersViews.as_view() , name='users_list'),

#     Friend request
    path('send-request/<int:id>/', SendFriendRequest.as_view(), name='send_request'),
    path('my-networks/', MyNetworksView.as_view(), name='networks'),
    path('add-networks/<int:id>/', AddFriendRequest.as_view(), name='add_networks'),
    path('delete-friend/<int:id>/', DeleteFriend.as_view(), name='delete_friend'),
    path('ignore-friend/<int:id>/', IgnoreFriendRequest.as_view(), name='ignore_friend'),
]
