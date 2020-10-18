from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Departments(models.TextChoices):
        ADMIN = "admin", "Admin"
        FINANCE = "finance", "Finance"
        PROGRAM = "program", "Program"
        MnE = "m&e", "M&E"
        COMMUNICATIONS = "communications", "Communications"
        IT = "it", "IT"

    department = models.CharField(max_length=20, choices=Departments.choices)

    class Roles(models.TextChoices):
        STAFF = "staff", "Staff"
        ADMINISTRATOR = 'adminstrator', 'Adminstrator'

    role = models.CharField(max_length=12, choices=Roles.choices, default=Roles.STAFF)
    image = models.ImageField(upload_to='users/images/', default='default.png')

    REQUIRED_FIELDS = ['email', 'department']

    def __str__(self):
        return self.username
