from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post

SCHOOL_CHOICES = [
    ('SEET', 'School of Engineering & Engineering Technology'),
    ('SOC', 'School of Computing'),
    ('SET', 'School of Environmental Technology'),
    ('SPS', 'School of Physical Science'),
    ('SLS', 'School of Life Science'),
    ('SHHT', 'School of Health and Health Technology'),
    ('SLIT', 'School of Logisties and innnovative Technology')
]

class Registerform(UserCreationForm):
    email = forms.EmailField(required=True)
    school = forms.ChoiceField(choices=SCHOOL_CHOICES, label="Your school", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100)
    fullname = forms.CharField(max_length=190, required=True)

    class Meta:
        model = User
        fields = ["fullname", "username", "email", "school"]

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["description"]