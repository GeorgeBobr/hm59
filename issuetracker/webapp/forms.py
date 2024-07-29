from django.forms import widgets
from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
from webapp.models import Type, Status, Project, Issue
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'types', 'status']


class TypeForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['start_data', 'end_data', 'title', 'description']


class ProjectUserForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Project
        fields = ['users']

class StatusForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')