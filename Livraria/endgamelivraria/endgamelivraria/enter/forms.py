# _*_ coding:utf-8 _*_
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models  import User
from django.forms.widgets import ClearableFileInput
from .models import *


# chama a tabela auth_user do banco de dados para criar um cadastro de usuario

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

# o widjets são parametros para o formulario.
Widgets = {
    'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255},),
    'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
    'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
    'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
    'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength':255}),
}

#personalizar menssagens de erro

error_messages = { 
    'first_name': {
        'required': 'Este campo é obrigatório!'
    },
    'last_name': {
        'required': 'Este campo é obrigatório!'
    },
    'username': {
        'required': 'Este campo é obrigatório!'
    },
    'password': {
        'required': 'Este campo é obrigatório!'
    },
    'email': {
        'required': 'Este campo é obrigatório!'
    },
}

#class LivroModelForm(forms.ModelForm):
#    foto = forms.ImageField(widget=ClearableFileInput)
#    
#    class Meta:
#        model = Livro
#        fields = '__all__'
#        widgets = {
#            'nome': forms.TextInput(attrs={'class':'form-control', 'maxlength': 255}),
#            'descricao': forms.Textarea(attrs={'class':'form-control', 'maxlength': 255}),
#            'idioma': forms.TextInput(attrs={'class':'form-control', 'maxlength': 255}),
#
#        }