from django import forms

class LoginFrm(forms.Form):
    userid = forms.CharField(max_length=80, label='아이디', required=True)
    