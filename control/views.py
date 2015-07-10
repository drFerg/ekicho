from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from .models import RollingStock
from django.template.context_processors import csrf
from EngineRoom.engineClient import EngineClient


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
e = EngineClient(UDP_IP, UDP_PORT)


@ensure_csrf_cookie
def trainStatus(request):
    c = {'stock': RollingStock.objects.all()}
    c.update(csrf(request))
    print c
    return render_to_response('control/index.html', c)


def updateSpeed(request):
    train = RollingStock.objects.get(id=request.POST['id'])
    train.speed = int(request.POST['speed'])
    train.save()
    e.setSpeed(train.address, train.speed, train.direction)
    return HttpResponse("DOne")


def updateDir(request):
    train = RollingStock.objects.get(id=request.POST['id'])
    train.direction = int(request.POST['dir'])
    train.speed = 0
    train.save()
    e.setDirection(train.address, train.direction)
    return HttpResponse(train.direction)


def getSpeed(request):
    train = RollingStock.objects.get(id=request.POST['id'])
    return HttpResponse(train.speed)
