from django.urls import path

from . import views



urlpatterns = [
    path('', views.ListAppView.as_view(), name='list-app'),
    path('app/<int:pk>/detail/', views.DetailAppView.as_view(), name='detail-app'),
    path('app/create/', views.CreateAppView.as_view(), name='create-app'),
    path('app/<int:pk>/delete/', views.DeleteAppView.as_view(), name='delete-app'),
    path('app/<int:pk>/update/', views.UpdateAppView.as_view(), name='update-app'),
    path('app/current_location', views.current_location, name='current_location'),
]