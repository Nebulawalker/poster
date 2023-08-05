from django.db import models

class Place(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    annotation = models.CharField(
        verbose_name='Краткое описание',
        max_length=400
    )
    full_description =models.TextField(
        verbose_name='Полное описание'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'