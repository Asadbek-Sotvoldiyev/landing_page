from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, ProfileForm,ResetPasswordForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User,FriendRequest


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('users:login')
        return render(request, 'users/register.html', {'form':form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'users/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('index')

class ProfileView(View):
    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, 'users/profile.html', {'form':form})
    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'users/profile.html', {'form':form})

class Profile(View):
    def get(self, request):
        return render(request, 'users/profile_view.html')

class UsersViews(LoginRequiredMixin,View):
    def get(self,request):
        users = User.objects.exclude(username=request.user.username)
        users_without_request_user_friends = users.exclude(friends=request.user)
        requests = FriendRequest.objects.filter(from_user=request.user)
        to_users = []
        for req in requests:
            to_users.append(req.to_user)
        return render(request, 'users/users.html',{"users":users_without_request_user_friends, 'requests':to_users})


class SendFriendRequest(LoginRequiredMixin, View):
    def get(self,request,id):
        to_user = User.objects.get(id=id)
        from_user = request.user

        FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
        return redirect('users:users_list')

class MyNetworksView(LoginRequiredMixin, View):
    def get(self, request):
        networks = FriendRequest.objects.filter(to_user=request.user, is_accepted=False)
        my_friends = request.user.friends.all()
        return render(request, 'users/networks.html', {"networks":networks,'my_friends':my_friends})

class AddFriendRequest(LoginRequiredMixin, View):
    def get(self,request,id):
        friend_request_user = FriendRequest.objects.get(id=id)
        from_user = friend_request_user.from_user
        main_user = request.user

        friend_request_user.is_accepted = True
        friend_request_user.save()
        main_user.friends.add(from_user)
        from_user.friends.add(main_user)

        return redirect('users:networks')

class DeleteFriend(LoginRequiredMixin, View):
    def get(self,request,id):
        user = request.user
        friend_to_delete = get_object_or_404(user.friends, id=id)

        try:
            friend_request = FriendRequest.objects.get(from_user=friend_to_delete, to_user=user)
            friend_request.delete()
        except:
            friend_request = FriendRequest.objects.get(to_user=friend_to_delete, from_user=user)
            friend_request.delete()

        user.friends.remove(friend_to_delete)
        friend_to_delete.friends.remove(user)

        return redirect('users:networks')

class IgnoreFriendRequest(LoginRequiredMixin, View):
    def get(self,request,id):
        friend_to_ignore = get_object_or_404(FriendRequest, to_user=request.user)
        friend_to_ignore.delete()

        return redirect('users:networks')

class ResetPasswordView(LoginRequiredMixin, View):
    def get(self,request):
        form = ResetPasswordForm()
        return render(request, 'users/reset_password.html',{"form":form})

    def post(self,request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']

            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return redirect('users:login')
        return render(request, 'users/reset_password.html', {"form": form})