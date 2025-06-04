from django.shortcuts import render
from .models import RonakVarity, Store
from django.shortcuts import get_object_or_404
from .forms import RonakVarityForm

# Create your views here.
def all_ronak(request):
    ronaks = RonakVarity.objects.all()
    return render(request, 'ronak/all_ronak.html',{'ronaks': ronaks}) 

def ronak_detail(request, ronak_id):
    ronak = get_object_or_404(RonakVarity, pk=ronak_id) 
    return render(request, 'ronak/ronak_detail.html', {'ronak': ronak}) 

def ronak_store_view(request):
    stores = None
    if request.method == 'POST':
        form = RonakVarityForm(request.POST)
        if form.is_valid():
            ronak_varity = form.cleaned_data['ronak_varity']
            stores = Store.objects.filter(ronaks=ronak_varity)
    else:
        form = RonakVarityForm()
    return render(request, 'ronak/ronak_store.html',{'stores': stores,'form': form}) 