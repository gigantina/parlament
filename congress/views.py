from pyexpat import model
from tempfile import template
from django.forms import fields
from django.shortcuts import render
from django.views.generic import CreateView, ListView
#from .models import User


def index(request):
    print(request.user)
    return render(
        request,
        'index.html')
