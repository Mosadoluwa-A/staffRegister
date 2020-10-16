from django.db import models


class User(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=50)

    class Departments(models.TextChoices):
        NOT_SELECTED = ""
        ADMIN = "admin", "Admin"
        FINANCE = "finance", "Finance"
        PROGRAM = "program", "Program"
        MnE = "m&e", "M&E"
        COMMUNICATIONS = "communications", "Communications"
        IT = "it", "IT"

    department = models.CharField(max_length=20, choices=Departments.choices, default=Departments.NOT_SELECTED)

    class Roles(models.TextChoices):
        STAFF = "staff", "Staff"
        ADMINISTRATOR = 'adminstrator', 'Adminstrator'

    role = models.CharField(max_length=12, choices=Roles.choices, default=Roles.STAFF)
    image = models.ImageField(upload_to='users/images/', default='default.png')

    def __str__(self):
        return self.name
