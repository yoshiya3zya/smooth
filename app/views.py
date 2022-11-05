from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )
from  .models import App

def current_location(request):
    return render(request,'app/current_location.html')


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






