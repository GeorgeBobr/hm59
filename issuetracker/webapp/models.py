from django.db import models
from django.utils import timezone

class Status(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class Type(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

class Project(models.Model):
    start_data = models.DateField()
    end_data = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False)
    description = models.TextField(max_length=2000, verbose_name='Описание')

class Issue(models.Model):
    summary = models.CharField(max_length=50, verbose_name="Заголовок", unique=True, null=False, blank=False)
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Описание')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    types = models.ManyToManyField(Type)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"