from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib import admin
from app.models import Account

def favorite(request):
    return render(request, 'accounts/favorite.html')

def completion(request):
    return render(request, 'accounts/completion.html')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def searched(request):
    return render(request, 'accounts/searched.html')

def reserve(request):
    return render(request, 'accounts/reserve.html')

class SignupView(CreateView):
    model = Account
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:completion')

