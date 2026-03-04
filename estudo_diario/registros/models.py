from django.db import models
from django.utils import timezone

class RegistroEstudo(models.Model):
    titulo_aula = models.CharField(max_length=200)
    data = models.DateField(default=timezone.now)
    resumo = models.TextField()
    dificuldade = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=1
    )

    def __str__(self):
        return f"{self.titulo_aula} ({self.data})"
