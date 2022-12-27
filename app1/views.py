from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def abhi(request):
    return HttpResponse('<h1><marquee>I LOVE YOU</marquee></h1>')
def abcd(request):
    return HttpResponse("<h2>GoodD MorninG</h2>")
def abc(request):
    return HttpResponse('<h2><marque> Good Morning </marque></h2>')