from django import forms

from .models import Volunteer

class PostForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('name', 'phone', 'role')