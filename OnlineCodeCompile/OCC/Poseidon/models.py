from django.db import models

# Create your models here.
class Code(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=20)
