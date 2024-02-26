from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


SCHOOL_CHOICES = [
    ('SEET', 'School of Engineering Technology'),
    ('SOC', 'School of Computing'),
    ('SET', 'School of Environmental Technology'),
    ('SPS', 'School of Physical Science'),
    ('SLS', 'School of Life Science'),
    ('SHHT', 'School of Health and Health Technology')
]

class Registerform(UserCreationForm):
    email = forms.EmailField(required=True)
    school = forms.ChoiceField(choices=SCHOOL_CHOICES, label="choose a school", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "email", "school"]