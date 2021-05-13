from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

import datetime


# Create your models here.
class Tour(models.Model):
    tour_date = models.DateField(default=timezone.localdate,
                                 verbose_name="Дата", blank=False)
    tour_name = models.CharField(max_length=100, blank=False,
                                 verbose_name="Название")
    tour_tickets = models.SmallIntegerField(default=100,
                                            verbose_name="Количество",
                                            blank=False)
    tour_distance = models.FloatField(blank=False, verbose_name="Расстояние")

    def __str__(self):
        return self.tour_name

    def save(self, *args, **kwargs):
        if self.tour_tickets < 0 or self.tour_tickets > 100:
            raise ValidationError("Tickets cannot be less than 0 "
                                  "and more than 100")
        if self.tour_date < datetime.date.today():
            raise ValidationError("Date cannot be smaller than today's date!")
        if self.tour_distance < 0:
            raise ValidationError("Distance cannot be negative")

        super(Tour, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
        ordering = ['tour_date']
