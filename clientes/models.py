from django.db import models


class CPF(models.Model):
    # Variavel definida para o numero do documento, recebe no maximo 50 caracteres
    num_doc = models.CharField(max_length=50)

    # Função para retornar o numero do documento no django admin
    def __str__(self):
        return self.num_doc


class Person(models.Model):
    # Variavel definida para o primeiro nome, recebe no maximo 50 caracteres
    first_name = models.CharField(max_length=50)
    # Variavel definida para o ultimo nome, recebe no maximo 50 caracteres
    last_name = models.CharField(max_length=50)
    # Variavel definida para a idade, recebe um valor inteiro
    age = models.IntegerField()
    # Variavel definida para descrição, recebe um texto
    bio = models.TextField()
    # Variavel definida para a foto
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    # Variavel definida para o cpf, recebe um valor da classe CPF
    cpf = models.OneToOneField(to=CPF, on_delete=models.CASCADE)

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    # Função para retornar o numero do documento no django admin
    def __str__(self):
        return self.first_name + ' ' + self.last_name
