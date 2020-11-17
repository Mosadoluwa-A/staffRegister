from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from day.models import Day
# from users.models import User


class PunctualManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(time_status="early")


class LateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(time_status="late")


class PunctualityManager(models.Manager):
    def get_punctual(self):
        return self.get_queryset().filter(time_status="early")

    def get_late(self):
        return self.get_queryset().filter(time_status="late")


class Clockin(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, null=True, on_delete=models.SET_NULL, related_name="clockins")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    time_in = models.TimeField(null=True, blank=True, default=datetime.now())
    time_out = models.TimeField(null=True, blank=True)
    TIMES = (
        ('early', 'Early'),
        ('late', 'Late'),
    )
    time_status = models.CharField(max_length=5, choices=TIMES, null=True)
    objects = PunctualityManager()
    punctual = PunctualManager()
    late = LateManager()

    def punc_stat(self):
        if self.time_in.hour < 8:
            status = "early"
        else:
            status = "late"
        return status

    def __str__(self):
        return self.name

    def make_slug(self):
        slug = slugify(self.name)
        return slug

    def save(self, *args, **kwargs):
        if not self.slug and not self.time_status:
            self.slug = self.make_slug()
            self.time_status = self.punc_stat()
        super().save(*args, **kwargs)
