from django.http import HttpResponse
from django.shortcuts import render
from . models import Place ,team
def demo(request):
    obj=Place.objects.all()
    tobj =team.objects.all()
    return render(request,"index.html",{'result': obj ,'tresult': tobj})
# Create your views here.
