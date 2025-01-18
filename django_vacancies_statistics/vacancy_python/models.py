from django.db import models


class MainPage(models.Model):
    content = models.TextField(blank=True, verbose_name='Описание профессии')
    photo = models.ImageField(upload_to='images_db/%Y/%m/%d', verbose_name='Фото')


class Demand(models.Model):
    salary_graph = models.ImageField(upload_to='images_db/%Y/%m/%d', verbose_name='График уровня зарплат')
    vacancy_graph = models.ImageField(upload_to='images_db/%Y/%m/%d', verbose_name='График количества вакансий')
    table = models.TextField(verbose_name='Таблица востребованности')


class Geography(models.Model):
    salary_graph_by_city = models.ImageField(upload_to='images_db/%Y/%m/%d', verbose_name='График зарплат по городам')
    vacancy_fraction_by_city = models.ImageField(upload_to='images_db/%Y/%m/%d', verbose_name='График доли вакансий по городам')
    table = models.TextField(verbose_name='Таблица географии')


class Skills(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название таблицы')
    table = models.TextField(verbose_name='Таблица')
    skills_graph = models.ImageField(upload_to='images_db/%Y/%m/%d', verbose_name='График по скиллам')


class LastVacancy(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    vacancy_name_to_parse = models.TextField(verbose_name='Вакансия для парсинга')
