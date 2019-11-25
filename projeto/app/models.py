from django.db import models


class Proprietario(models.Model):
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    nome = models.CharField(max_length=50, null=False, default=None)
    data_nascimento = models.DateField(
        null=False, verbose_name='Data de Nascimento', default=None)
    cpf = models.CharField(max_length=20, null=False, default=None)
    profissao = models.CharField(max_length=20, null=False, default=None)
    telefone = models.CharField(max_length=20, null=False, default=None)

    def __str__(self):
        return self.nome


class Acessorios(models.Model):
    ESTADO_CHOICES = (
        ('otimo', 'Otimo'),
        ('bom', 'Bom'),
        ('ruim', 'Ruim'),
    )
    descricao = models.CharField(max_length=100, null=False, default=None)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.descricao
    
class Veiculo(models.Model):
    CORES_CHOICES = (
        ('preto','Preto'),
        ('azul','Azul'),
        ('amarelo','Amarelo'),
        ('branco','Branco'),
        ('prata','Prata'),
        ('vermelho','Vermelho'),
    )
    TIPO_CHOICES = (
        ('moto','Moto'),
        ('carro','Carro'),
    )

    modelo = models.CharField(max_length=50, null=False, default=None)
    marca = models.CharField(max_length=30,null=False,default=None)
    placa = models.CharField(max_length=15,null=False,default=None)
    cor = models.CharField(max_length=10,choices=CORES_CHOICES)
    ano = models.IntegerField(null=False, default=None)
    preco = models.FloatField(null=False, default=None)
    foto_capa = models.ImageField(upload_to='imagens')
    tipo = models.CharField(max_length=5,choices=TIPO_CHOICES)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField('Acessorios')

    def __str__(self):
        return self.modelo