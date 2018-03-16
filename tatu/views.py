import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def index(request):
    context_dict = {}
    image_list = os.listdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media'))
    context_dict['images'] = image_list
    return render(request, 'tatu/index.html', context=context_dict)

#def about(request):
#    return HttpResponse("""About page
#    <a href="/tatu/">Index</a>""")


    #user = UserProfile.objects.get(pk=1)
    #image_list = user.images.all()

def contact(request):
    return HttpResponse("""Contact us page
    <a href="/tatu/">Index</a>""")

def faq(request):
    return HttpResponse("""FAQ page
    <a href="/tatu/">Index</a>""")

def register(request):
    return HttpResponse("""Register page
    <a href="/tatu/">Index</a>""")

def login(request):
    return HttpResponse("""Login page
    <a href="/tatu/">Index</a>""")

def artists(request):
    return HttpResponse("""Artists page
    <a href="/tatu/">Index</a>""")

def tattoos(request):
    return HttpResponse("""Tattoos page
    <a href="/tatu/">Index</a>""")

