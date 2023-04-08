from django.db import models

# Create your models here.
class fack_user(models.Model):
    id = models.AutoField(primary_key=True)
    User_name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    Password = models.CharField(max_length=500)
    Confirm_Password = models.CharField(max_length=500)

