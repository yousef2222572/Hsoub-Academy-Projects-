from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


attrs={'class':'form-control'}


class UserLoginForm(AuthenticationForm):

    def __init__(self,*args, **kwargs):
        super(UserLoginForm,self).__init__( *args, **kwargs)
        
        
    username=forms.CharField(
        label=_('User name'),
        widget=forms.TextInput(attrs=attrs)
    )
    password=forms.CharField(
        label=_('Password'),
        widget=forms.TextInput(attrs=attrs)
    )

class UserFormCreation(UserCreationForm):
    
    
    def __init__(self,*args,**kwargs):
        super(UserFormCreation,self).__init__(*args,**kwargs)
        
    first_name=forms.CharField(
        label=_('first name'),
        widget=forms.TextInput(attrs=attrs)
    )
    last_name=forms.CharField(
        label=_('last name'),
        widget=forms.TextInput(attrs=attrs)
    )

    username=forms.CharField(
        label=_('user name'),
        widget=forms.TextInput(attrs=attrs)
    )
    email=forms.EmailField(
        label=_('email'),
        widget=forms.TextInput(attrs=attrs)
    )
    password1=forms.CharField(
        label=_('password'),
        widget=forms.PasswordInput(attrs=attrs)
    )
    password2=forms.CharField(
        label=_('passwor confirm'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )
    
    class Meta (UserCreationForm.Meta):
        fields=('first_name','last_name','username','email')
        
        
class UserProfileView(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email'] 
        labels={
            'first_name':_('first name'),
            'last_name':_('last name'),
            'email':_('email')
        }
        
        widgets={
            'first_name':forms.TextInput(attrs=attrs),
            'last_name':forms.TextInput(attrs=attrs),
            'email':forms.TextInput(attrs=attrs)
        }
        
