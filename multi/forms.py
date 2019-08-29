from .models import Multi
from django import forms

class MultiForm(forms.ModelForm):
    class Meta:
        model = Multi
        fields = ('number_x', 'number_y')
        
    def multi(self):
        return self.cleaned_data['number_x'] * self.cleaned_data['number_y']