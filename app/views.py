from django.shortcuts import render
import json, datetime,  calendar, locale
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
        locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
        # 日付のリスト生成()
        date_list = [datetime.today() + timedelta(days=i) for i in range(14)]
        # 文字列に変換
        hour_list = []
        for hour in range(24):
            hour_list.append(datetime(year=datetime.today().year, month=datetime.today().month, day=datetime.today().day, hour=hour))
        #hour_list = [datetime(hour=hour) for hour in range(24)]
        date_str_list = [d.strftime("%Y年%m月%d日%A") for d in date_list]
        context = super().get_context_data(*args, **kwargs)
        context["date_str_list"] = date_str_list 
        context["date_list"] = date_list
        context["hour_list"] = hour_list
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

def Booking_confirmation(request):
    print(request.GET['place_id'], request.GET['reserve_date'])
    # reserve_date = datetime.strptime(request.GET['reserve_date'], 'YmdHi')
    place = Place.objects.get(id=request.GET['place_id'])
    return render(request,'app/booking_confirmation.html', {'place': place})

 






