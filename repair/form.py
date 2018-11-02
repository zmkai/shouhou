from django import forms


class ReceivedForm(forms.Form):
    weibao_account = forms.CharField(max_length=32)


class ReceivingForm(forms.Form):
    number_id = forms.CharField(max_length=32)


class UnReceiveForm(forms.Form):
    weibao_account = forms.CharField(max_length=32)

