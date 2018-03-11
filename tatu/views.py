from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("""Index page. Tatu
    <br/> <a href='/tatu/about/'>About</a>
    <br/> <a href='/tatu/contact-us/'>Contact us</a>
    <br/> <a href='/tatu/FAQ/'>FAQ page</a>
    <br/> <a href='/tatu/register/'>Register page</a>
    <br/> <a href='/tatu/login/'>Login page</a>
    <br/> <a href='/tatu/artists/'>Artists page</a>
    <br/> <a href='/tatu/tattoos/'>Tattoos page</a>""")

def about(request):
    return HttpResponse("""About page
    <a href="/tatu/">Index</a>""")

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

