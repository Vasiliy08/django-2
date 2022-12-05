from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class AllEmployees(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    INN = models.CharField(max_length=15, verbose_name="ИНН")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    slug = models.SlugField(unique=True, db_index=True, verbose_name="Идентификатор")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Должность')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Должность")
    slug = models.SlugField(unique=True, db_index=True, verbose_name="Идентификатор")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"