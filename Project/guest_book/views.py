from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Record
from .forms import RecordSearchForm, RecordForm

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

def record_add(request):
    if request.method=='GET':
        form = RecordForm()
        return render(request, 'record_add.html', context={'form':form})
    elif request.method=='POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = Record.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                text=form.cleaned_data.get('text')
            )
            return redirect('record-list')
        return render(request, 'record_add.html', context={'form':form})

def record_update(request, pk):
    record = get_object_or_404(Record, id=pk)
    if request.method=='GET':
        form=RecordForm(
            initial={
             'name':record.name,
             'email':record.email,
             'text':record.text
            }
        )
        return render(request, 'record_update.html',context={'record':record,'form':form})
    elif request.method == "POST":
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record.name = form.cleaned_data.get('name')
            record.email = form.cleaned_data.get('email')
            record.text = form.cleaned_data.get('text')
            record.save()
            return redirect('record-list')
        return render(request, 'record_update.html', context={'record':record, 'form':form})
