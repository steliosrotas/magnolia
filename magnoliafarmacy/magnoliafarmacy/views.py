#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Magnolia Farmacy Home Page")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("About our Farmacy")