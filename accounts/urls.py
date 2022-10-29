from django.urls import path
from django.contrib.auth.views import  LoginView, LogoutView
from . import views
from .views import SignupView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('favorite/', views.favorite, name='favorite'), 
    path('completion/', views.completion, name='completion'),
    path('mypage/', views.mypage, name='mypage'),
    path('searched/', views.searched, name='searched'),
    path('reserve/', views.reserve, name='reserve')

]