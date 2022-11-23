from django.shortcuts import render
import json, datetime
from datetime import date, timedelta, datetime
from .google_maps_api import geocode
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )
from .models import App, Place, PlacePhoto


def current_location(request):
    place_queryset = Place.objects.all()
    for item in place_queryset:
        lat, lng = geocode(item.address)
        print(item.address,lat, lng)
        item.lat = lat
        item.lng = lng
        item.save()
    place_json = json.dumps(list(place_queryset.values()))
    return render(request,'app/current_location.html',{'place_json': place_json})

def detail(request):
    place_photo_list = PlacePhoto.objects.all()
    return render(request,'app/detail.html')


class ListAppView(ListView):
    template_name = 'app/app_list.html'
    model = App

class DetailAppView(DetailView):
    template_name = 'app/app_detail.html'
    model = Place
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['one_week'] = [1,2,3,4,5,6,7]
        context["new_date"] = date.today()
        context["tomorrow_date"] = datetime.now() + timedelta(days=1)
        return context
    
  

class CreateAppView(CreateView):
    template_name = 'app/app_create.html'
    model = App
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('list-app')

class DeleteAppView(DeleteView):
    template_name = 'app/app_confirm_delete.html'
    model = App
    success_url = reverse_lazy('list-app')

class UpdateAppView(UpdateView):
    model = App
    fields = ('title', 'text', 'category')
    template_name = 'app/app_update.html'
    success_url = reverse_lazy('list-app')






