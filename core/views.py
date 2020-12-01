from django.shortcuts import render, redirect
from crawler import urls

# Create your views here.
def index(request):

    return redirect('crawler:index')