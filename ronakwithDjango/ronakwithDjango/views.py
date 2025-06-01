from django.http import HttpResponse
from django.shortcuts import render

def home(request):
      return render(request, 'website/index.html')
def about(request):
    return HttpResponse("<h1>Welcome to Ronak's Django App in About</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Ronak's Django App in Contact</h1>")