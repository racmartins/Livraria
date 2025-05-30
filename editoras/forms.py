from django import forms
from .models import Editora


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'endereco', 'website', 'email', 'telefone', 'logo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }
