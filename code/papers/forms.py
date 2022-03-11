from django import forms

class PaperForm(forms.Form):
    title = forms.CharField(label='title')
    authors = forms.CharField(label='authors')
    abstract = forms.CharField(label='abstract')
    docUrl = forms.CharField(label='docUrl')
    logoUrl = forms.CharField(label='logoUrl')