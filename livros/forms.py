from django import forms
from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'editora', 'categoria', 'isbn',
                  'data_publicacao', 'capa', 'descricao', 'preco']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Insira o título do livro'
            }),
            'autores': forms.SelectMultiple(attrs={
                'class': 'form-control select2',
                'data-placeholder': 'Selecione os autores'
            }),
            'editora': forms.Select(attrs={
                'class': 'form-control select2',
                'data-placeholder': 'Selecione a editora'
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Insira a categoria'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Insira o ISBN'
            }),
            'data_publicacao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'capa': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',  # Aceita apenas arquivos de imagem
                'data-preview': 'true'  # Atributo personalizado para ativar preview
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Insira a descrição do livro'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if self.instance.pk:  # Se estiver editando
            if Livro.objects.filter(isbn=isbn).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Este ISBN já está registado.')
        else:  # Se estiver criando
            if Livro.objects.filter(isbn=isbn).exists():
                raise forms.ValidationError('Este ISBN já está registado.')
        return isbn

    def clean_capa(self):
        capa = self.cleaned_data.get('capa')
        if capa:
            # Verifica se é uma imagem
            if not capa.content_type.startswith('image'):
                raise forms.ValidationError(
                    'Por favor, envie apenas arquivos de imagem.')

            # Verifica o tamanho do arquivo (max 5MB)
            if capa.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    'O tamanho máximo permitido é 5MB.')

            # Lista de extensões permitidas
            allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
            import os
            ext = os.path.splitext(capa.name)[1][1:].lower()
            if ext not in allowed_extensions:
                raise forms.ValidationError(
                    f'Extensão não permitida. Use: {", ".join(allowed_extensions)}')

        return capa

    def save(self, commit=True):
        livro = super().save(commit=False)

        # Se uma nova imagem foi enviada e já existe uma imagem antiga
        if 'capa' in self.changed_data and self.instance.pk and self.instance.capa:
            # Importa os módulos necessários
            import os
            from django.conf import settings

            # Tenta excluir o arquivo antigo
            try:
                old_capa_path = os.path.join(
                    settings.MEDIA_ROOT, str(self.instance.capa))
                if os.path.isfile(old_capa_path):
                    os.remove(old_capa_path)
            except Exception as e:
                print(f"Erro ao excluir imagem antiga: {e}")

        if commit:
            livro.save()
            self.save_m2m()  # Salva as relações many-to-many

        return livro
