from pyexpat import model
from tempfile import template
from django.forms import fields
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
#from .models import User


def index(request):
    return redirect('index')