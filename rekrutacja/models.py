from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Uczelnia(models.Model):
    nazwa = models.CharField(max_length=100)
    rodzaj = models.CharField(max_length=50)
    adres = models.CharField(max_length=200)
    data_zalozenia = models.DateField()
    numer_uczelni_nadany_przez_ministra = models.IntegerField(unique=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.nazwa

    class Meta():
        verbose_name = "Uczelnia"
        verbose_name_plural = "Uczelnie"


class KierunekStudiow(models.Model):
    STOPIEN_CHOICES = (
        ('I stopień', 'I stopień'),
        ('II stopień', 'II stopień'),
        ('jednolite', 'jednolite')
    )
    TRYB_CHOICES = (
        ('stacjonarne', 'stacjonarne'),
        ('niestacjonarne', 'niestacjonarne'),
        ('online', 'online'),
        ('hybrydowe', 'hybrydowe'),
    )
    TYP_CHOICES = (
        ('licencjackie', 'licencjackie'),
        ('inżynierskie', 'inżynierskie'),
    )

    nazwa = models.CharField(max_length=100)
    uczelnia = models.ForeignKey(Uczelnia, on_delete=models.CASCADE)
    stopien = models.CharField(max_length=20, choices=STOPIEN_CHOICES)
    tryb = models.CharField(max_length=20, choices=TRYB_CHOICES)
    typ = models.CharField(max_length=20, choices=TYP_CHOICES, blank=True, null=True)
    opis = models.TextField(blank=True, null=True)
    rok_akademicki = models.CharField(max_length=9)

    def __str__(self):
        return self.nazwa

    def clean(self):
        if self.stopien != 'I stopień' and self.typ:
            raise ValidationError(
                {'typ': 'Pole "typ" może być uzupełnione tylko dla kierunków studiów stopnia "I stopień".'})
        if self.stopien == 'I stopień' and not self.typ:
            self.typ = "licencjackie"

    class Meta():
        verbose_name = "Kierunek Studiów"
        verbose_name_plural = "Kierunki Studiów"
