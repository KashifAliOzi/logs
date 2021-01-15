from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from MiniFb import settings
from .forms import CreateUserForm, PostUpdateForm
from .models import *
from django.core.mail import send_mail
from MiniFb.settings import *
from django.contrib.sessions.models import Session
import json

def index(request):
    return HttpResponse("Testing")


def registerPage(request):
    if request.session.has_key('is_logged'):
        return redirect('socialapp:userposts')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                # subject = 'Email Verification'
                # message = 'http://127.0.0.1:8000/verifylogin/?token=1234'
                # recepient = request.POST.get('email')
                # send_mail(subject,
                #           message, EMAIL_HOST_USER, [recepient], fail_silently=False)
                return redirect('socialapp:login')
        form = CreateUserForm()
        context = {}
        context['form'] = form
        return render(request, 'register.html', context)


def userLogin(request):
    # if request.session.has_key('is_logged'):
    #     return redirect('socialapp:userposts')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        rememberMe = False
        try:
            rememberMe = request.POST['rememberme']
            rememberMe = True
        except:
            rememberMe = False
        print('rem me:', rememberMe)
        usr = authenticate(request, username=username, password=password)
        if usr is not None:
            login(request, usr)
            request.session['is_logged'] = True
            if rememberMe==True:
                request.session.set_expiry(900)
            else:
                request.session.set_expiry(30)
            return redirect('socialapp:userposts')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


@login_required
def logoutUser(request):
    logout(request)
    return redirect('socialapp:login')


@login_required
def newPost(request):
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        return redirect('socialapp:userposts')
    form = PostUpdateForm()
    context = {'form': form}
    return render(request, 'new_post.html', context)


@login_required
def userPostsPage(request):
    posts = BlogPost.objects.filter(user=request.user)
    context = {'posts': posts, 'media_url': settings.MEDIA_URL}
    return render(request, 'user_posts.html', context)


@login_required
def postdetail(request, id):
    post = BlogPost.objects.filter(id=id)
    context = {'post': post, 'media_url': settings.MEDIA_URL}
    return render(request, 'post_detail.html', context)


@login_required
def updatePost(request, id):
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
    #     title = request.POST.get('title')
    #     description = request.POST.get('description')
    #     try:
    #         image = request.FILES.get('picture')
    #         BlogPost.objects.filter(id=id).update(title=title, image=image, description=description)
    #     except:
    #         BlogPost.objects.filter(id=id).update(title=title, description=description)
    #
        return redirect('socialapp:userposts')

    inst = BlogPost.objects.get(id=id)
    form = PostUpdateForm(request.POST, request.FILES, instance=inst)
    context = {'form': form, 'media_url': settings.MEDIA_URL}
    return render(request, 'new_post.html', context)


@login_required
def deletePost(request, id):
    BlogPost.objects.filter(id=id).delete()
    return redirect('socialapp:userposts')


def verifyEmail(request):
    key = 1234
    token = request.GET.get('token')
    if int(token) == key:
        return redirect('socialapp:login')
    else:
        return HttpResponse('invalid token')

def emailDuplicationChecker(request):
    temp = Users.objects.filter(email=request.GET.get('email')).count()
    if temp > 0:
        return JsonResponse({"status": False})
    else:
        return JsonResponse({"status": True})
