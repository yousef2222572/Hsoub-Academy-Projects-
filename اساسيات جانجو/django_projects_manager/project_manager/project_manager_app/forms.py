from django import forms 
from . import models
from django.utils.translation import gettext as _
attrs={'class':'form-control'}

class Projectcreateform(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=['title','category','description']
        widgets={
            'title':forms.TextInput(attrs=attrs),
            'category':forms.Select(attrs=attrs),
            'description':forms.Textarea(attrs=attrs)
        }
class Projectupdateform(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=['title','status','category']
        labels={
            'category':_('Category'),
            'status':_('status'),
            'title':_('title')
        }
        widgets={
            'title':forms.TextInput(attrs=attrs),
            'category':forms.Select(attrs=attrs),
            'status':forms.Select(attrs=attrs)
        }