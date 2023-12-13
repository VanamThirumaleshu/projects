from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Members
# Create your views here.

def details(request):

    
    
    
    return render(request,'practice/exp.html')
def showdetails(request):
    data=Members.objects.all().values()


    return render(request,'practice/details.html',{'data':data})
def insert(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        member=Members.objects.create(first_name=first_name,last_name=last_name)
        data=Members.objects.all().values()
    return render(request,'practice/details.html',{'data':data})