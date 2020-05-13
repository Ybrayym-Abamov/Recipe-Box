from django import forms
from recipe.models import Author, RecipeItem


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    instructions = forms.CharField(widget=forms.Textarea)


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
