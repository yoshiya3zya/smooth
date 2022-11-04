from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib import admin
from app.models import Account, PlacePhoto
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    Posts = Post.objects.order_by('created_date').reverse()
    paginator = Paginator(Posts, 5)
    page = request.GET.get('page', 1)
    try:
    	pages = paginator.page(page)
    except PageNotAnInteger:
    	pages = paginator.page(1)
    except EmptyPage:
    	pages = paginator.page(1)
    context = {'pages': pages}
    return render(request, 'mypage.html', context)

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


