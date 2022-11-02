from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def homepage(request):
#    return HttpResponse("Hi! Welcome to the innovation with python training.")

def homepage(request):
    return render(request,'detailfolder/home.html')
def indexpage(request):
    return render(request,'detailfolder/index.html')