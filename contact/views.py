from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView, 
    DetailView, 
    UpdateView,
    DeleteView,
)
from .models import Contact
from .forms import ContactForm

# Create your views here.
class ContactListView(ListView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm

class ContactDetailView(DetailView):
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm

class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')