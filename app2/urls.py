from django.urls import path
from app2.views import *

app_name='xyz'

urlpatterns=[
    path('abcd/',abcd,name='abcd'),
    path('abc/',abc,name='abc')
]