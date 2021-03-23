from django.urls import path
from .views import ContactListView, ContactCreateView, ContactDetailView

urlpatterns = [
  path("", ContactListView.as_view(), name="contact_list"),
  path("new/", ContactCreateView.as_view(), name="contact_create"),
  path("detail/<int:pk>", ContactDetailView.as_view(), name="contact_detail")
  # /detail/1
]