from django.db import models


class Direction(models.Model):
    title = models.CharField(max_length=150, verbose_name="Напрямок")
    slug = models.SlugField(max_length=150, verbose_name="URL", unique=True)
    sort_number = models.DecimalField(max_digits=10, decimal_places=0, unique=True, verbose_name="Номер сортування")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Напрямок'
        verbose_name_plural = 'Напрямки'
        ordering = ['sort_number']


class Doctor(models.Model):
    title = models.CharField(max_length=150, verbose_name="Лікарь")
    slug = models.SlugField(max_length=150, verbose_name="URL", unique=True)
    directions = models.ManyToManyField(Direction, blank=False, related_name='direction')
    education = models.TextField(blank=None, null=False, verbose_name='Освіта')
    birthday = models.DateField(verbose_name="Дата народження")
    description_of_experience = models.TextField(blank=None, null=False, verbose_name='Досвід опис')
    years_of_experience = models.DecimalField(max_digits=2, decimal_places=0, verbose_name="Досвід років")
    sort_number = models.DecimalField(max_digits=10, decimal_places=0, unique=True, verbose_name="Номер сортування")

    def display_directions(self):

        return ','.join([direction.title for direction in self.directions.all()[:3]])

    display_directions.short_description = 'Напрямок'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лікар(я)'
        verbose_name_plural = 'Лікарі'
        ordering = ['sort_number']
