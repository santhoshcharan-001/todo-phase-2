import re

from django.http.response import HttpResponse,JsonResponse

from django.shortcuts import render,redirect

from .models import Tasks

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Create your views here.


@login_required(login_url='/')
def get_tasks(request):
    objs=Tasks.objects.filter(username=request.user)
    li=[]
    for ele in objs:
        dic={}
        dic["id"] = ele.id
        dic["title"]=ele.title
        dic["description"]=ele.description
        dic["time"]=ele.time
        dic["date"]=ele.date
        dic["priority"]=ele.priority
        dic["status"]=ele.status
        li.append(dic)
    return JsonResponse({"data":li})

@login_required(login_url='/')
def delete(request):
    id = request.GET.get("id")
    obj=Tasks.objects.filter(id=id,username=request.user)
    if obj.exists():
        obj[0].delete()
    return JsonResponse({})
    
@login_required(login_url='/')
def add_task(request):
    print("add_task")
    title=request.GET.get("title")
    des=request.GET.get("des")
    priority=request.GET.get("priority")
    date=request.GET.get("date")
    time=request.GET.get("time")
    status=request.GET.get("status")
    username=str(request.user)
    print(title,request.GET.get("adding"))
    if request.GET.get("adding")=="true":
        form=Tasks.objects.create(title=title,description=des,priority=priority,date=date,time=time,status=status,username=username)
        form.save()
        print("saved")
        return JsonResponse({ "id" : form.id })
    else:
        edit_id=request.GET.get("edit_id")
        r=Tasks.objects.filter(id=edit_id).update(title=title,description=des,
        priority=priority,date=date,time=time,status=status,username=username)
        return HttpResponse("ok")


def login_arti(request):
    print("login arti")
    print(request.user)
    # if
    if request.user.is_authenticated:
        print("already logged in")
        return render(request,"home.html")
    return render(request,'basic.html')

def validate_login(request):
    print("validate_login")
    try:
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        print(username,password)
        print(user)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            print("logged in")
            return redirect('/home/')
        else:
            return render(request,'basic.html',{'error':'Invalid username or password'})
            # No backend authenticated the credentials
    except:
        print("error")
        return redirect('/')


# @login_required(login_url='/')
def home(request):
    print(request.user)
    if request.user.is_authenticated:
        print("already logged in")
        return render(request,"home.html")
    else:
        return render(request,'basic.html')

def logout_arti(request):
    try:
        logout(request)
        return redirect('/')
    except:
        return redirect('/')

def register(request):
    try:
        print("register")
        username=request.POST.get('username-register')
        password=request.POST.get('password-register')
        print(username,password)
        # repassword=str(request.POST['repassword'])
        obj=User.objects.create_user(username=username,password=password)
        print("about to save")
        obj.save()
        return redirect('/home/')
    except:
        print("failed to register this user")
        return redirect('/')
        


def check_username(request):
    print("check_username")
    username=str(request.GET['username'])
    print(username)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'status':'Username already taken'})
    else:
        return JsonResponse({'status':'Username available'})