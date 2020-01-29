from django import forms
from .models import Facility


class Facility_form(forms.ModelForm):

    class Meta:
        model = Facility
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'cols': 35, 'maxlength': 50, 'class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
        fields = ['name', 'description', 'thumbnail']
