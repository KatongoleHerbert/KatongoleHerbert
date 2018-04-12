# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin

# Register your models here.
from accounts.models import User


my_default_errors2 = {
    'required': 'Student Number is required',
}

my_default_errors3 = {
    'required': 'Password is required',
}

my_default_errors4 = {
    'required': 'Retype password is required',
}


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        if not 'initial' in kwargs:
            kwargs['initial'] = {}
    std_id = forms.CharField(error_messages=my_default_errors2,widget=forms.TextInput())
    password1 = forms.CharField(error_messages=my_default_errors3,widget=forms.PasswordInput())
    password2 = forms.CharField(error_messages=my_default_errors4,widget=forms.PasswordInput())
    course = forms.CharField(max_length=30, required=False, widget=forms.TextInput())
    year = forms.IntegerField(required=False, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('std_id',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
