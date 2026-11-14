from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView

from users.models import User
from .forms import UserRegisterForm, UserLoginForm

# Create your views here.

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        send_mail(subject, message, None, recipient_list)

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'