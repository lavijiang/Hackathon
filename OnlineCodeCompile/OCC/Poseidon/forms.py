from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        field = ['code']
        exclude = ()