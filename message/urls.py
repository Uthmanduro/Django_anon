from django.urls import path
from . import views

urlpatterns = [
    path('anon', views.MessageAPI.as_view())
]