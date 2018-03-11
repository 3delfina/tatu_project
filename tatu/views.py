from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("""Index page. Tatu
    <br/> <a href='/tatu/about/'>About</a>""")

def about(request):
    return HttpResponse("""About page
    <a href="/tatu/">Index</a>""")
