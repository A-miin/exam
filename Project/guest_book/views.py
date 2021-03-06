from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Record
from .forms import RecordSearchForm

# Create your views here.
def index(request):
    form = RecordSearchForm()
    if request.method=='GET':
        records = Record.objects.all().filter(status='active').order_by('-created_at')
        return render(request, 'index.html', context={'records':records, 'form':form})
    elif request.method=='POST':
        name = request.POST.get('name')
        records = Record.objects.all().filter(name=name, status='active').order_by('-created_at')
        return render(request, 'index.html', {'records':records, 'form':form})

