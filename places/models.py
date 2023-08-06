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

class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        verbose_name='Фотография'
    )
    index = models.SmallIntegerField(
        verbose_name='Порядок',
        default=0,
        db_index=True
    )
    class Meta: 
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['index']

    def __str__(self):
        return f'{self.index}) {self.place}'
