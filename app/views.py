from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from app.models import Beer, Restaurant, UserProfile

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beer'] = Beer.objects.all()
        context['restaurant'] = Restaurant.objects.all()
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant

class BeerListView(ListView):
    pass

class BeerDetailView(DetailView):
    model = Beer
