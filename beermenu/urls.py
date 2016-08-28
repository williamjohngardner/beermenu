from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, login

from app.views import IndexView, RestaurantDetailView, BeerListView,     BeerDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^restaurant/(?P<pk>\d+)/$', RestaurantDetailView.as_view(), name="restaurant_detail_view"),
    url(r'^beer_list/$', BeerListView.as_view(), name="beer_list_view"),
    url(r'^beer_list/(?P<pk>\d+)/$', BeerDetailView.as_view(), name="beer_detail_view")
]
