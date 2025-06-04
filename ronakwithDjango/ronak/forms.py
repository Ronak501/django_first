from django import forms
from .models import RonakVarity

class RonakVarityForm(forms.Form):
    ronak_varity = forms.ModelChoiceField(
        queryset=RonakVarity.objects.all(),
        empty_label="Select Ronak Varity",  
        label="Ronak Varity"
    )