from django.urls import path, re_path
from . import views

# path('', views.index, name='index'),

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('message/new/', views.MessageCreateView.as_view(), name='message_new'),
    path('alum/new/', views.AlumCreateView.as_view(), name='alum_new'),
    path('messages/filter', views.MessageFilterView.as_view(), kwargs=None, name='message_filter'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
]
