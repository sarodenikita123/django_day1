from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
