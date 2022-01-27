from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('faq', faq, name='faq'),
    path('portfolio', portfolio, name='portfolio'),
      path('blogs', blogs, name='blogs'),
]
