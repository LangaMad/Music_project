from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Singer,Gruop,Music
# Create your views here.


class SingersView(ListView):
    model = Singer
    template_name ='singers.html'
    context_object_name ='singers'
    queryset = Singer.objects.all()


class GroupsView(ListView):
    model = Gruop
    template_name = 'groups.html'
    context_object_name = 'groups' # object_list
    queryset = Gruop.objects.all()


class GroupsDetailView(DetailView):
    model = Gruop
    template_name = 'groups_detail.html'
    context_object_name = 'group'
    queryset = Gruop.objects.all()

class SingerDetailView(DetailView):
    model = Singer
    template_name = 'singer_detail.html'
    context_object_name = 'singer'
    queryset = Singer.objects.all()

class MusicListView(ListView):
    model = Music
    template_name = 'music_list.html'
    context_object_name = 'musics'
    queryset = Music.objects.all()



