from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
# Create your views here.
class AtamaListAPIView(ListCreateAPIView):
    queryset = Atama.objects.all()
    serializer_class = AtamaSerializer

def home(request):
    atama = Atama.objects.all()
    return render(request,'home.html')