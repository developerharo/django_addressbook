from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Contact
from .forms import ContactCreate

# Create your views here.
class ContactListView(ListView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactCreate

class ContactDetailView(DetailView):
    model = Contact