from django import forms

from collab.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ['id', 'user']


class SearchForm(forms.Form):
    date = forms.DateField()