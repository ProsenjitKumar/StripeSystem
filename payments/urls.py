from django.conf.urls import re_path
from .views import *

urlpatterns = [
    re_path('^$', HomeView.as_view(), name='home'),
    re_path('charge/', charge, name='charge'),
]