from django.shortcuts import render

# Create your views here.
def all_ronak(request):
    return render(request, 'ronak/all_ronak.html')    