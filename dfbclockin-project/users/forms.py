from django.forms import ModelForm
from .models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'username', 'password', 'role']