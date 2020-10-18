from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.text import slugify

# from users.models import User


class Clockin(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    time_in = models.TimeField(null=True, blank=True, default=datetime.now())
    time_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def make_slug(self):
        slug = slugify(self.name)
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.make_slug()
        super().save(*args, **kwargs)