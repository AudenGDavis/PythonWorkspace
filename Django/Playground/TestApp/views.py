from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestAppFunc(request):
    return render(request,"Main.html")