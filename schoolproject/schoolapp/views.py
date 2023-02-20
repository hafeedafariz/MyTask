from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Department,Course



# Create your views here.
def allcourses(request,c_slug=None):
    c_page=None
    courses=None
    Null = False
    if c_slug!=None:
        c_page=get_object_or_404(Department,slug=c_slug)
        courses= Course.objects.all().filter(department=c_page,)
    else:
        courses= Course.objects.all().filter(seats=True)
    return render(request, "department.html", {'department': c_page,'courses': courses})
def courseDetail(request,c_slug,course_slug):
    try:
        course=Course.objects.get(department_slug=c_slug,slug=course_slug)
    except Exception as e:
        raise e
    return render(request,'course.html',{'course':course})
def registerlink(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('register')
    return render(request,"register.html")
def newpage(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('newpage')
    return render(request,"newpage.html")
def form(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('form')
    return render(request,"form.html")
def lastmsg(request):
    return render(request, "lastmsg.html")
