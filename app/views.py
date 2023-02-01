from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insertion successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=='POST':
        topic=request.POST.get('topic')
        name=request.POST['name']
        url=request.POST.get('url')
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        return HttpResponse('Webpage is created')
    return render(request,'insert_webpage.html',d)

def insert_Access(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    if request.method=='POST':
        topic=request.POST.get('topic')
        name=request.POST['name']
        url=request.POST.get('url')
        date=request.POST['date']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        A=AccessRecord.objects.get_or_create(date=date)[0]
        A.save()
        return HttpResponse('insertion successfully')
    return render(request,'insert_Access.html',d)

def select_multiple(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    if request.method=='POST':
        t=request.POST.getlist('topic')
        qsw=Webpage.objects.none()
        for i in t:
            qsw=qsw|Webpage.objects.filter(topic_name=i)
        dic={'webpages':qsw}
        return render(request,'display_webpages.html',dic)
    return render(request,'select_multiple.html',d)

def checkbox(request):
    qst=Topic.objects.all()
    d={'topic':qst}
    return render(request,'checkbox.html',d)

def delete(request):
    Topic.objects.filter(topic_name=' ').delete()
    return HttpResponse('delete')