from django.db import models


class Day(models.Model):
    name = models.CharField(max_length=50)
    month = models.CharField(max_length=9)
    year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
