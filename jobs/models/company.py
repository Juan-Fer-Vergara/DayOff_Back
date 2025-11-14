from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=150)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
