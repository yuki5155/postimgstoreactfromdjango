from django.db import models

class TodoApp(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

