from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=15)
    staff_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name