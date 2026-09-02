from django import forms
from django_app.models import Author ,tag,Article


field_attrs={'class':'form-control mb-2'}


# class Articlesform(forms.Form):
#     title=forms.CharField(min_length=10,max_length=20)
#     content=forms.CharField()
#     author_id=forms.ModelChoiceField(Author.objects.all())
#     tags=forms.ModelMultipleChoiceField(tag.objects.all())

class Authorform(forms.Form):
    name=forms.CharField(max_length=40)
    email=forms.EmailField()
    birthdate=forms.DateField(required=False)
    bio = forms.CharField(required=False,widget=forms.Textarea)

class Articlesform(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','content','author','tag']
        widgets={
            'title':forms.TextInput(attrs=field_attrs),
            'content':forms.Textarea(attrs=field_attrs),
            'author':forms.Select(attrs=field_attrs),
            'tag':forms.SelectMultiple(attrs=field_attrs)
        }