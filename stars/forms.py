from django import forms

class StarsForm(forms.Form):
    number_id=forms.CharField(max_length=32)
    star = forms.CharField(required=True)

