from django.urls import path,include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('home/',index,name='home'),
    url('view',CountryAPIView.get_queryset),
    url('api',CountryAPIView.as_view()),
]