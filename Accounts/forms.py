from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .choices import GENDER

YEARS = [x for x in range(1940, 2021)]


class SignUpForm(UserCreationForm):

    Gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'birthdate', 'Gender', 'address', 'profile']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_member = True
        user.save()
        return user


