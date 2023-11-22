from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy

# Create your views here.


class RegisterView(CreateView):
    template_name ='register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')



