from django import forms
from pot.models import Pot

class PotForm(forms.ModelForm):
    class Meta:
        model = Pot
        fields = ('number_x', 'number_y')
