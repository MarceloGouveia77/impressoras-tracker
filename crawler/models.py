from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=50, null=False)

    def __str__(self):
        return self.nome

NOMES_IMPRESSORAS = [
    (1, 'BROTHER DCP6250DW',)
]
class Impressora(models.Model):
    ip = models.CharField('Endereço IP', max_length=15, null=False)
    nome = models.CharField('Nome', choices=NOMES_IMPRESSORAS, max_length=50)
    departamento = models.ForeignKey(Departamento, related_name="Departamento", on_delete=models.CASCADE)
    nivel_toner = models.DecimalField("Nível Toner", decimal_places=2, max_digits=3)
    status = models.CharField('Status', max_length=50)

    def __str__(self):
        return self.nome + ' - ' + self.departamento.nome