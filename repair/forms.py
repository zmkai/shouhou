from django import forms

class RepairForm(forms.Form):
    customer_id=forms.CharField(max_length=32)
    depot_id=forms.CharField(max_length=32)
    title = forms.CharField(max_length=20)
    problem_desciption = forms.CharField(max_length=255)

class RepairForm1(forms.Form):
    page=forms.CharField(max_length=2)
    pageSize=forms.CharField(max_length=1)

class RepairForm2(forms.Form):
    title = forms.CharField(max_length=20,required=False)
    problem_desciption = forms.CharField(max_length=255,required=False)
