from django.db import models


class LastVacancyModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
