from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Uavs

def index(request):
    uavs = Uavs.objects
    return render(request, "uavs/index.html", {"uavs" : uavs})

def detail(request, uav_id):
    uav_detail = get_object_or_404(Uavs, pk=uav_id)
    return render(request, "uavs/detail.html", {"uav": uav_detail})

def home(request):
    homs = Uavs.objects
    return render(request, "uavs/home.html", {"homs": homs})

