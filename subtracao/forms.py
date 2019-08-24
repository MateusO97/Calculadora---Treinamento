from django import forms
from .models import Operacao

class SubForm(forms.ModelForm):

    class Meta:
        model = Operacao
        fields = ('number1', 'number2',)
