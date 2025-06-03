from django.shortcuts import render
from .models import RonakVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_ronak(request):
    ronaks = RonakVarity.objects.all()
    return render(request, 'ronak/all_ronak.html',{'ronaks': ronaks}) 

def ronak_detail(request, ronak_id):
    ronak = get_object_or_404(RonakVarity, pk=ronak_id) 
    return render(request, 'ronak/ronak_detail.html', {'ronak': ronak}) 