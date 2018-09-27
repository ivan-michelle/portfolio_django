from django import forms

class ProjectForm (forms.Form):
    title = forms.CharField(label='Title', required=True)
    description = forms.CharField(label='Description', required=True)
    image = forms.ImageField(label='Logo', required=True)
    link = forms.URLField(label='www', required=True)
