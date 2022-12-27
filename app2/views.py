from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def abcd(request):
    return HttpResponse('<h2>Hello ....12/27/2022---tuesday</h2>')
def abc(request):
    return HttpResponse('<h3>i think all are good</h3>')