from django.db import models

'''
Id -> O id será gerado automaticamente pelo Django
Nome
Email
CPF
Data de Nascimento
Número de celular   
'''

class Estudante (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=100)
    cpf = models.CharField(max_length=11, blank=False)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14, blank=False)
 
    def __str__(self):
        return self.nome



class Cursos(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, blank=False, null=False)
    nivel = models.CharField(max_length=1, blank=False, null=False, choices=NIVEL, default='B')

    def __str__(self):
        return self.codigo