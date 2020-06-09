from django.forms import ModelForm
from .models import Person, CPF


# Formulário da classe person
class PersonForm(ModelForm):
    class Meta:
        model = Person
        # Dados que serão preenchidos no formulario, nesse caso, todos
        fields = '__all__'


# Formulário da classe cpf
class CPFForm(ModelForm):
    class Meta:
        model = CPF
        # Dados que serão preenchidos no formulario, nesse caso, todos
        fields = '__all__'