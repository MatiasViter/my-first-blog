import imp
from urllib.parse import urlparse
from django.urls import path
from .  import views

urlpatterns = [
    path ('', views.post_list, name='post_list'),
]