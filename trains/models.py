from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Train(models.Model):
    COMMUTER = 'CMTR'
    SHINKANSEN = 'SHKN'
    FREIGHT = 'FRGT'
    TRAIN_TYPES = (
        (COMMUTER, 'Commuter'),
        (SHINKANSEN, 'Shinkansen'),
        (FREIGHT, 'Freight')
        )
    manufacturer = models.ForeignKey(Manufacturer)
    type = models.CharField(max_length=4,
                            choices=TRAIN_TYPES,
                            default=COMMUTER)
    series = models.CharField(max_length=20)
    name = models.CharField(max_length=100, blank=True)
    length = models.IntegerField()
    icon = models.ImageField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return "[" + self.manufacturer.name + "] " + self.series
