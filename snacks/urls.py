from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomeView , about


urlpatterns = [
    path ('' , HomeView.as_view(), name='home'),
    path ('about' , about.as_view() , name='about')
]