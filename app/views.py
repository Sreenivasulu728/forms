from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def insert(request):    
    if request.method=='POST':
        to=request.POST['to']
        TO=Topic.objects.get_or_create(topic_name=to)[0]
        TO.save()
        return HttpResponse('data inserted successfully')
    return render(request,'insert.html')
    return render(request,'models.py')

def options(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        top=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        email=request.POST['email']

        TO=Topic.objects.get(topic_name=top)
        WO=Webpages.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('DATA inserted successfully')
    return render(request,'options.html',d)

        