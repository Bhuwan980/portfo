import imp
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
	portfolios = Portfolio.objects.all()
	blogs = Blogs.objects.all()
	
	context = {'portfolios':portfolios, 'blogs':blogs}
	return render(request, 'home.html', context=context)


def contact (request):
	return render(request, 'contact.html')

def about (request):
	return render(request, 'about.html')

def faq (request):
	return render(request, 'faq.html')

def portfolio (request):
	portfolios = Portfolio.objects.all()
	context = {'portfolios':portfolios}
	return render(request, 'portfolio.html', context=context)


def blogs (request):
	context = { 'blog': Blogs.objects.all()}

	return render(request, 'blogs.html', context)