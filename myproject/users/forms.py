from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'phone', 'avatar', 'country']


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')