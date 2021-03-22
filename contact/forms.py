from django import forms
from .models impor Contact

class ContactCreate(forms.ModelForm):
  class Meta:
    model = Contact
    fields = "__all__"