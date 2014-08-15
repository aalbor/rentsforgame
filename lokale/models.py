from django.db import models
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


# Create your models here.

class Juego(models.Model):
    id = models.AutoField(primary_key=True)
    prop = models.ForeignKey('lokale.Client', blank=True, null=True)
    adres = models.CharField('Adres', max_length=50)
    miasto = models.CharField('Miasto', max_length=30)
    licz_pokoi = models.IntegerField('Liczba pokoi')
    cena = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    data_wyp = models.DateField('Data wypozyczenia', blank=True, null=True)
    data_odd = models.DateField('Data oddania', blank=True, null=True)
    opis = models.CharField('Opis', max_length=300)
    zdj_link = models.CharField('Link do zdjecia', max_length=200)
    def __unicode__(self):
        return str(self.adres) + ' ' + str(self.miasto)

    def __str__(self):
        return str(self.adres) + ' ' + str(self.miasto)

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nick = models.CharField('Login', max_length=20)
    cont = models.CharField('Contra',max_length=20)
    email = models.EmailField('E-Mail', blank=True, null=True)
    def __unicode__(self):
        return str(self.nick)
    def __str__(self):
        return str(self.nick)

class Protocolo(models.Model):
    id = models.AutoField(primary_key=True)
    lokal_id = models.ForeignKey('lokale.Juego')
    wlasciciel_id = models.ForeignKey('lokale.Client', related_name='wlasciciel_mieszkania')
    klient_id = models.ForeignKey('lokale.Client', related_name='klient_mieszkania')
    cena = models.DecimalField('Cena',max_digits = 10, decimal_places = 2)
    ilosc = models.IntegerField('Ilosc dni')
    data = models.DateField('Data')
    def __unicode__(self):
        return str(self.id) + ' ' + str(self.lokal_id) + ' ' + str(wlasciciel_id) + ' ' + str(self.klient_id)
