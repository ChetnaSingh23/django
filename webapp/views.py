from django.shortcuts import render
from django.http import HttpResponse

from json import loads
from urllib2 import urlopen


def index(request):
  data = loads(urlopen("http://httpbin.org/ip").read())
  return HttpResponse("<h1>The public IP is :</h1> %s" % data["origin"])




 

