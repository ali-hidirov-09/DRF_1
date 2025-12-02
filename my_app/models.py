from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    autor = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"