from django.db import models
import datetime
from django.utils import timezone

class Cliente(models.Model):
    email = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    data_nasc = models.DateField()
    telefone = models.CharField(max_length=255)
    fk_endereco_pk = models.IntegerField()
    senha = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    cod_cliente = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    codigo = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    numero_edicao = models.IntegerField()
    preco =  models.FloatField()
    foto = models.ImageField(null=True)

    def __str__(self):
        return self.nome


class Compra(models.Model):
    fk_cliente_cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fk_livro_codigo = models.ForeignKey(Livro, on_delete=models.CASCADE)
    valor_total = models.FloatField()
    data_compra = timezone.now()
    cod_compra = models.AutoField(primary_key=True)



class Reserva(models.Model):
    fk_cliente_cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    kf_livro_codigo = models.ForeignKey(Livro, on_delete=models.CASCADE)
    codigo_reserva = models.AutoField(primary_key=True)
    data_reserva = models.DateField()


