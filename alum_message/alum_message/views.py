from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.db.models import F, Q
from django_filters.views import FilterView


from .models import Message, Receipt, Alum
from .forms import MessageForm, AlumForm
from .filters import MessageFilter

# Create your views here.

class AboutPageView(generic.TemplateView):
    template_name = 'alum_message/about.html'

class HomePageView(generic.TemplateView):
    template_name = 'alum_message/home.html'

class MessageDetailView(generic.DetailView):
    model = Message
    context_object_name = 'message'
    template_name = 'alum_message/message_detail.html'

class MessageFilterView(FilterView):
    filterset_class = MessageFilter
    template_name = 'alum_message/message_filter.html'

class MessageCreateView(generic.View):
    model = Message
    form_class = MessageForm
    success_message = "Message created successfully"
    template_name = 'alum_message/message_new.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            message_new = form.save(commit=False)
            message_new.save()
            for uniqname in form.cleaned_data['recipients']:
                Receipt.objects.create(message=message_new, alum=uniqname)
            # return redirect(site) # shortcut to object's get_absolute_url()
            return HttpResponseRedirect(message_new.get_absolute_url())
        return render(request, 'alum_message/message_new.html', {'form': form})

    def get(self, request):
        form = MessageForm()
        return render(request, 'alum_message/message_new.html', {'form': form})

class AlumCreateView(generic.View):
    model = Alum
    form_class = AlumForm
    success_message = "Alum created successfully"
    template_name = 'alum_message/alum_new.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        form = AlumForm(request.POST)
        if form.is_valid():
            alum_new = form.save(commit=False)
            alum_new.save()
            return HttpResponseRedirect('/')
        return render(request, 'alum_message/alum_new.html', {'form': form})

    def get(self, request):
        form = AlumForm()
        return render(request, 'alum_message/alum_new.html', {'form': form})