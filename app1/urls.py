from django.urls import path
from app1.views import *

app_name="some"


urlpatterns=[
    path('abhi/',abhi,name='abhi'),
    path('abcd/',abcd,name='abcd'),
    path('abc/',abc,name='abc')
]