from django import forms

from Accounts.choices import GENDER
from Accounts.models import User
from .models import Auditorium


class Audi_form(forms.ModelForm):

    class Meta:
        model = Auditorium
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'cols': 35, 'maxlength': 50, 'class': 'form-control'}),
        }
        fields = ['description', 'booking_date']


class Updateform(forms.ModelForm):
    Gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = User
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 6, 'cols': 20, 'maxlength': 50, 'class': 'form-control'}),
        }
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'Gender', 'address', 'profile']
