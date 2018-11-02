from django import forms

class RepairForm_p(forms.Form):
    customer_id=forms.CharField(max_length=32)
    depot_id=forms.CharField(max_length=32)
    title = forms.CharField(max_length=20)
    problem_desciption = forms.CharField(max_length=255)

class RepairForm_g(forms.Form):
    page=forms.CharField(max_length=2)
    pageSize=forms.CharField(max_length=1)



class ReceivedForm(forms.Form):
    weibao_account = forms.CharField(max_length=32)


class ReceivingForm(forms.Form):
    number_id = forms.CharField(max_length=32)


class UnReceiveForm(forms.Form):
    weibao_account = forms.CharField(max_length=32)
