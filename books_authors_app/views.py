from django.shortcuts import render, redirect
from .models import Books, Authors

# Create your views here.

def index(request):
    context = {
        "all_authors": Authors.objects.all()    
    }
    return render(request,'index.html', context)
