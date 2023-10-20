from django.urls import path
from .views import *
urlpatterns = [
    path('api/',AtamaListAPIView.as_view()),
    path('',home)
]