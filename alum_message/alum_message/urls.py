from django.urls import path, re_path
from . import views

# path('', views.index, name='index'),

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
