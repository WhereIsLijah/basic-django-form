from django.db import models

class UserInfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    terms_condition = models.BooleanField() 