from django.db import models


class Tasks(models.Model):
    status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]

    description = models.TextField(
        verbose_name='Описание')
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='new',
        verbose_name='Статус'
    )
    date_to_complete = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата выполнения'
    )

    def __str__(self):
        return f'{self.description} {self.status}'