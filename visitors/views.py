from django.shortcuts import render,redirect
from visitors.models import Visitor

# Create your views here.

def show(request):
    visitors = Visitor.objects.all()
    return render(request,"show.html",{'visitor':visitors})

def home(request):
    #visitors = Visitor.objects.all()
    return render(request,"home.html")


def addVisitors(request):
    return render(request,"addVisitor.html")



def addVisitor(request):
        print("----------------- Inside addVisitor Function -------------")
        if request.method == 'POST':
            if(request.POST.get('fname') and request.POST.get('lname') and
		request.POST.get('gender') and request.POST.get('age')):
                visitor = Visitor()
                visitor.fname = request.POST.get('fname')
                visitor.lname = request.POST.get('lname')
                visitor.gender = request.POST.get('gender')
                visitor.age = request.POST.get('age')
                visitor.save()
                return render(request, 'home.html')
        else:
                return render(request,'home.html')

