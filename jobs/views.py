from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    jobs = Company.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        about = request.POST.get('about')
        worker = request.POST.get('worker')
        started = request.POST.get('started')
        value = request.POST.get('value')
        data = Company(boss=name,company_name=company,about=about,worker=worker,started=started,value=value)
        data.save()
        return redirect('/')
    return render(request,'index.html',{'jobs':jobs},)

def delete(request,pk):
    if request.method == 'POST':
        job = Company.objects.get(id=pk)
        job.delete()
        return redirect('/')
    return render(request,'delete.html')

