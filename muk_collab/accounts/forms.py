from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    std_id = forms.CharField(widget=forms.TextInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        std_id = self.cleaned_data.get('std_id')
        password = self.cleaned_data.get('password')
        user = authenticate(std_id=std_id, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        std_id = self.cleaned_data.get('std_id')
        password = self.cleaned_data.get('password')
        user = authenticate(std_id=std_id, password=password)
        return user


class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password", None)
        if not self.user.check_password(old_password):
            raise ValidationError('Incorrect password.')
        return old_password

    def clean_retype_new_password(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2