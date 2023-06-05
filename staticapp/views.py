from django.shortcuts import render
from . models import Place
from .models import Team
# Create your views here.
def demo(request):

    obj=Place.objects.all()
    members=Team.objects.all()
    dict={'res':obj,'team':members}
    return render(request,'index.html',dict)
