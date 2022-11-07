from django.shortcuts import render
import json
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )
from .models import App, Place

def current_location(request):
    data = {Place.objects.all()}
    seat_json = json.dumps(data)
    return render(request,'app/current_location.html',{'seat_json': seat_json})


class ListAppView(ListView):
    template_name = 'app/app_list.html'
    model = App

class DetailAppView(DetailView):
    template_name = 'app/app_detail.html'
    model = App

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






