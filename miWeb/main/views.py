from django.shortcuts import render
import random


def index(request):
    return render(request, 'main/index.html')



