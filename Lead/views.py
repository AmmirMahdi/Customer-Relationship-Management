from django.shortcuts import render
from django.views.generic import (
                                CreateView,
                                UpdateView,
                                DeleteView,
                                DetailView,
                                ListView)

from django.urls import reverse_lazy


from .serializers import LeadSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated   
from rest_framework import viewsets


from Lead.models import Lead


class LeadListView(ListView):
    model = Lead 
    context_object_name = 'leads'
    template_name = 'lead/list.html'

class LeadDetailView(DetailView):
    model = Lead 
    context_object_name = 'lead'
    template_name = 'lead/detail.html'

class LeadCreateView(CreateView):
    model = Lead 
    template_name = 'lead/create.html'
    fields = ['name',"email","phone","account","status","source","address","website","description","assigned_to","created_to","is_active","enqueryType"]

class LeadUpdateView(UpdateView):
    model = Lead 
    template_name = 'lead/update.html'
    fields = ['name',"email","phone","account","status","source","address","website","description","assigned_to","created_to","is_active","enqueryType"]

class LeadDeleteView(DeleteView):
    model = Lead 
    template_name = 'lead/delete.html'
    success_url = reverse_lazy('lead:list')





class ModelViewSet(viewsets.ModelViewSet):
    queryset         = Lead.objects.all()
    serializer_class = LeadSerializer 