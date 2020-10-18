from django.forms import ModelForm
from .models import Clockin


class ClockinForm(ModelForm):
    class Meta:
        model = Clockin
        fields = ['name', 'time_in']
