from django.shortcuts import render
from django.http import HttpResponse

from . models import Products

def index(request):
    fast = Products.objects.all()
    return render(request,'index.html',{'fast': fast})
def home(request):
    return HttpResponse('this is the home page it include all the things')
def product(request):
    return HttpResponse('this are the product in the page')
def about(request):
    return HttpResponse('about us')
def help(request):
    return HttpResponse(' this is the page for contacting us')                