from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class todo(models.Model):
    title       = models.CharField(max_length=30)
    created     = models.DateTimeField(auto_now_add=True)
    completed   = models.BooleanField(default=False)
    uid         = models.ForeignKey(profile, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.title

