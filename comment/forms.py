from django import forms

class CommentForm(forms.Form):
    number_id=forms.CharField(max_length=32)
    comments = forms.CharField(max_length=255)
    remark=forms.CharField(max_length=255,required=False)
