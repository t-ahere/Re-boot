from django.db import models


class Rec(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField(max_length=100, blank=True, default='')
