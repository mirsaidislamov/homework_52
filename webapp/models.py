from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Tasks(models.Model):

    description = models.TextField(
        verbose_name='Описание')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )
    date_to_complete = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата выполнения'
    )
    detailed_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Детальное описание'
    )

    def __str__(self):
        return f'{self.description} {self.status}'