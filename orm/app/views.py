from django.shortcuts import render

from app.models import *
from django.http import HttpResponse 

def insert_topic(request):
    tn=input("Enter topic name")
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        return HttpResponse('Object is Created successfully')
    else:
        return HttpResponse('this object is already existed')
def insert_webpage(request):
    tn=input("Enter your toipc name:")
    n=input("Enter the candidate Name:")
    u=input("Enter the url:")

    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    WO=webpage.objects.get_or_create(topic_name=TO,name=n,url=u)

    if WO[1]:
         return HttpResponse('Webpage is Created successfully')
    else:
        return HttpResponse('Webpage is already existed')
def insert_AccessRecord(request):
    tn=input("Enter the topic name:")
    n=input("Enter name:")
    a=input("Enter the author Name:")
    d=input("Enter the date:")
    u = input("Enter the URL:") 

    TO=Topic.objects.get_or_create(topic_name=n)[0]
    WO=webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)
    if AO[1]:
        return HttpResponse("yoyr webpage is created successfully")
    else:
        return HttpResponse("This webpage is alredy existed")

