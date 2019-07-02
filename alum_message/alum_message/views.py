from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.db.models import F, Q

# Create your views here.

class AboutPageView(generic.TemplateView):
    template_name = 'alum_message/about.html'

class HomePageView(generic.TemplateView):
    template_name = 'alum_message/home.html'