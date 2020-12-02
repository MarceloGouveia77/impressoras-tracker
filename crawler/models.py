from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=50, null=False)

    def __str__(self):
        return self.nome

MODELOS_IMPRESSORAS = [
    ('1', 'DCP-L5652DN',),
    ('2', 'DCP-L5502DN')
]

STATUS_IMPRESSORAS = [
    ('0', 'OFFLINE'),
    ('1', 'ONLINE'),
]
class Impressora(models.Model):
    ip = models.CharField('Endereço IP', max_length=15, null=False)
    modelo = models.CharField('Modelo', choices=MODELOS_IMPRESSORAS, max_length=50)
    departamento = models.ForeignKey(Departamento, related_name="Departamento", on_delete=models.CASCADE)
    nivel_toner = models.DecimalField("Nível Toner", decimal_places=2, max_digits=4)
    status = models.CharField('Status', choices=STATUS_IMPRESSORAS, max_length=50)
    obs = models.CharField('Obs', max_length=50, blank=True)

    def __str__(self):
        return self.modelo + ' - ' + self.departamento.nome