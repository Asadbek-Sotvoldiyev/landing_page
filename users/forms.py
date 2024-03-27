from django import forms
from users.models import User
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control w-100'}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control w-100'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control w-100'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-control w-100'}))
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control w-100'}))
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control w-100'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2!=password:
            raise forms.ValidationError("Passwords don't match")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username)<5 or len(username)>30:
            raise forms.ValidationError("Username 5 va 30 orasida bo'lishi kerak")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bunday email bazada mavjud")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control w-100'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control w-100'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username)<5 or len(username)>30:
            raise forms.ValidationError("Username 5 va 30 orasida bo'lishi kerak")
        return username

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control w-100'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'class': 'form-control w-100'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Last name', 'class': 'form-control w-100'}))
    email = forms.CharField(disabled=True ,label="", widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control w-100'}))
    image = forms.ImageField(label="", widget=forms.FileInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', "email", 'image']
