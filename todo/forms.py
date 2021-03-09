from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class todoform(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task'}))
    
    class Meta:
       model = todo
       fields = '__all__' 

    


class CreateUserForm(UserCreationForm):
    #email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    '''def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user    '''