from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import post

# Create your views here.
def index(request):
    posts = post.objects.all()
    user = request.user
    return render(request,'index.html',{'posts':posts ,'user':user})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username = username):
                messages.info(request,"User Already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Passwords does not match")
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')

def addPost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        subTitle = request.POST.get('subTitle')
        discription = request.POST.get("discription")
        image = request.FILES.get('image')

        post.objects.create(author = request.user , title = title , subtitle = subTitle, discription = discription, image = image )
        return redirect('index')
    else:
        return render(request,'addPost.html')

def yourPosts(request):
    yourPost = post.objects.filter(author = request.user)
    return render(request,'yourPosts.html',{'yourPost':yourPost})

def fullPost(request,pk):
    seeFullPost = post.objects.get(id = pk)
    return render(request,'fullPost.html',{'post':seeFullPost})

def profile(request):
    user = request.user
    return render(request,'profile.html',{'user':user})