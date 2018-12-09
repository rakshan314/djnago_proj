from django.contrib.auth.models import User
from django.db import models

class Hobby(models.Model):
    hobby = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.hobby

class Member(User):
    gender = models.CharField(max_length=6)
    date_of_birth = models.DateField()
    picture = models.ImageField(upload_to='profile_images')
    hobby = models.ManyToManyField(to=Hobby, blank=True, symmetrical=False)
