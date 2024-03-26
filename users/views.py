from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ProfileForm
from django.views import View
from django.contrib.auth import authenticate, login, logout

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
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'users/profile.html', {'form':form})

