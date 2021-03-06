from django.shortcuts import render
from .models import Record

# Create your views here.
def index(request):
    records = Record.objects.all().filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={'records':records})