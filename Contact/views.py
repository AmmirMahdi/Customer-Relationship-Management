from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Contact

class ContactListView(ListView):
    queryset = Contact.objects.all()
    context_object_name = 'contacts'
    template_name = 'contact/list.html'


class ContactDetailView(DetailView):
    queryset = Contact.objects.all() 
    context_object_name = 'contact'
    template_name = 'contact/detail.html'

  
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contact/create.html'
    fields = ['first_name',"last_name","account","email","phone","address","description",]

class ContactUpdateView(UpdateView):
    model = Contact 
    template_name = 'contact/update.html'
    fields = ['first_name',"last_name","account","email","phone","address","description"]

class ContactDeleteView(DeleteView):
    model = Contact 
    template_name = 'contact/delete.html'
    success_url = reverse_lazy('contact:list')

