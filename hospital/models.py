from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    malade = models.BooleanField(default=False)
    def __str__(self):
        return self.title
