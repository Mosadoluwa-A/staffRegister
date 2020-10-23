from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    # class Departments(models.TextChoices):
    #     ADMIN = "admin", "Admin"
    #     FINANCE = "finance", "Finance"
    #     PROGRAM = "program", "Program"
    #     MnE = "m&e", "M&E"
    #     COMMUNICATIONS = "communications", "Communications"
    #     IT = "it", "IT"

    DEPARTMENTS = (
        ("Admin", "Admin"),
        ("Finance", "Finance"),
        ("Program", "Program"),
        ("M&E", "M&E"),
        ("Communications", "Communications"),
        ("IT", "IT"),
    )

    department = models.CharField(max_length=20, choices=DEPARTMENTS)

    # class Roles(models.TextChoices):
    #     STAFF = "staff", "Staff"
    #     ADMINISTRATOR = 'administrator', 'Administrator'

    ROLES = (
        ("staff", "Staff"),
        ('administrator', 'Administrator'),
    )

    role = models.CharField(max_length=13, choices=ROLES, default=ROLES[0])
    image = models.ImageField(upload_to='users/images/', default='default.png')

    REQUIRED_FIELDS = ['email', 'department']

    def __str__(self):
        return self.username
