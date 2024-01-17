from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название датчика')
    description = models.CharField(max_length=50, null=True, verbose_name='Описание датчика')


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура при измерении')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время измерения')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
