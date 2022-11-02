from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib import admin
from app.models import Account, PlacePhoto


ITEM_PER_PAGE = 10

def favorite(request):
    return render(request, 'accounts/favorite.html')

def completion(request):
    return render(request, 'accounts/completion.html')

def mypage(request):
    place_photo_list = PlacePhoto.objects.all()
    return render(request, 'accounts/mypage.html', {'place_photo_list': place_photo_list})

def searched(request):
    return render(request, 'accounts/searched.html')

def reserve(request):
    return render(request, 'accounts/reserve.html')

class SignupView(CreateView):
    model = Account
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:completion')

