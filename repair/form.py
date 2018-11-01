from django import forms


class RepairForm(forms.Form):
    number_id = forms.CharField(max_length=32)

class GetStarsForm(forms.Form):
    weibao_account = forms.CharField(max_length=32)