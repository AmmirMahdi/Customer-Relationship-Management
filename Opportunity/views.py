from django.shortcuts import render, redirect
from django.views.generic import (
                                CreateView,
                                UpdateView,
                                DeleteView,
                                DetailView,
                                ListView)

from django.urls import reverse_lazy

from .models import Opportinuty
from .serializers import OpportinutySerializer
from rest_framework.response import Response 
from rest_framework import viewsets
#################################################################

################################################################
from Lead.models import Lead


class OOPListView(ListView):
    model = Opportinuty
    context_object_name = 'oops'
    template_name = 'list.html'

class OOPDetailView(DetailView):
    model = Opportinuty 
    context_object_name = 'oop'
    template_name = 'detail.html'

class OOPCreateView(CreateView):
    model = Opportinuty 
    template_name = 'create.html'
    fields = ['name',"account","stage","lead_souce","probility","contacts","closed_by","description","created_by","is_active"]

class OOPUpdateView(UpdateView):
    model = Opportinuty 
    template_name = 'update.html'
    fields = ['name',"account","stage","lead_souce","probility","contacts","closed_by","description","created_by","is_active"]

class OOPDeleteView(DeleteView):
    model = Opportinuty
    template_name = 'delete.html'
    success_url = reverse_lazy('oop:list')



class ModelViewSetOPP(viewsets.ModelViewSet):
    queryset         = Opportinuty.objects.all()
    serializer_class = OpportinutySerializer 

