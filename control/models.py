from django.db import models
from trains.models import Train


class RollingStock(models.Model):
    STOPPED = 'STP'
    FORWARD = 'FWD'
    BACKWARD = 'BWD'
    BRAKING = 'BRK'
    TRAIN_STATUS = (
        (STOPPED, 'Stopped'),
        (FORWARD, 'Forward'),
        (BACKWARD, 'Backward'),
        (BRAKING, 'Braking')
        )
    train = models.ForeignKey(Train)
    address = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    status = models.CharField(max_length=3,
                              choices=TRAIN_STATUS)
    direction = models.IntegerField(default=2)

    def __str__(self):
        return self.train.__str__() + " (" + self.status + ")"
