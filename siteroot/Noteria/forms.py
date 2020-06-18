from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label='E-Mail', max_length=256)
    password = forms.CharField(label='Password', max_length=1024, min_length=3, widget=forms.PasswordInput)
    password_again = forms.CharField(label='Password, again', max_length=1024, min_length=3, widget=forms.PasswordInput)