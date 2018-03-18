import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tatu.models import *
from tatu.forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from .forms import ContactForm

# Create your views here.

def index(request):
    context_dict = {}
    test = Post.objects.all().order_by('-favourites').values_list('image', flat=True)
    test = list(test)
    print(test)
#    image_list = Post.objects.g
#    all_commenter_ids = Post.objects..order_by('-id').values_list('submitted_by', flat=True)[:25]
#all_commenter_ids = list(all_commenter_ids)
#    context_dict['images'] = image_list
    return render(request, 'tatu/index.html', context=context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.save()
            registered = True

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request,
                  'tatu/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                    'registered': registered
                   })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled.")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'tatu/login.html', {})


def artists(request):
    return HttpResponse("""Artists page
    <a href="/tatu/">Index</a>""")

def tattoos(request):
    return HttpResponse("""Tattoos page
    <a href="/tatu/">Index</a>""")

def about(request):
    return HttpResponse("""About page
    <a href="/tatu/">Index</a>""")


    #user = UserProfile.objects.get(pk=1)
    #image_list = user.images.all()

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "tatu/contact.html", {'form': form})
  

    

def faq(request):
    context_dict = {}
    image_list = os.listdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media'))[1:4]
    context_dict['images'] = image_list
    return render(request, 'tatu/faq.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_post(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user

            if 'image' in request.FILES:
                post.image = request.FILES['image']
                post.save()
            else:
                print(post_form.errors)
    else:
        post_form = PostForm()

    return render(request, 'tatu/upload.html', {'post_form': post_form
                                                })


def successView(request):
    context_dict = {}
    return render(request, "tatu/success.html", context=context_dict)
