from django.forms import ModelForm
from clockin.models import Absent


class AbsentForm(ModelForm):
    class Meta:
        model = Absent
        fields = ['staff', 'reason']
