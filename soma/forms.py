from django import forms

from .models import Soma

class SomaForm(forms.ModelForm):

    class Meta:
        model = Soma
        fields = ('number1', 'number2', 'result',)