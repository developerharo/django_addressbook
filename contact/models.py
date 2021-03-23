from django.db import models
from django.urls import reverse


class Contact(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=20, blank=True)
  email = models.EmailField(blank=True)
  address = models.TextField(blank=True)

  def __str__(self):
    return f"{self.last_name}, {self.first_name}"

  def get_absolute_url(self):
    return reverse("contact_detail", kwargs={"pk": self.pk})