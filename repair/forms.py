from django import forms

class RepairForm(forms.Form):
    customer_id=forms.CharField(max_length=32)
    depot_id=forms.CharField(max_length=32)
    title = forms.CharField(max_length=20)
    problem_desciption = forms.CharField(max_length=255)