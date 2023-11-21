from django.db import models
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField
from PIL import Image
from django.utils.translation import gettext_lazy as _

# Create your models here.


class AutomobilioModelis(models.Model):
    # automobilio modelis
    marke = models.CharField(_('Car make'), max_length=40, null=False, help_text=_('Enter car maker'))
    modelis = models.CharField(_('Car model'), max_length=40, null=False,
                               help_text=_('Enter car model'))

    class Meta:
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return f'{self.marke} {self.modelis}'


class Automobilis(models.Model):
    # automobilis pagal modeli ir valst.nr+vin+klientas
    valstybinis_nr = models.CharField(_('License plate number'),
                                      max_length=7, null=False, unique=True, help_text=_('Enter licence plate number'))
    automobilio_modelis_id = models.ForeignKey('AutomobilioModelis', verbose_name=_('Car model'),
                                               on_delete=models.CASCADE, null=False)
    vin_kodas = models.CharField(max_length=17, null=False, unique=True, help_text=_('enter VIN code'))
    klientas = models.CharField(max_length=100, null=False,
                                help_text=_('Enter client (organisation name or name/surname'))
    nuotrauka = models.ImageField(_('Photo'), upload_to='nuotraukos', null=True)
    aprasymas = HTMLField()

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

    def __str__(self):
        return f'{self.valstybinis_nr}, {self.automobilio_modelis_id}, {self.klientas}'


class Uzsakymas(models.Model):
    # uzsakymas kuriame gali buti daug uzsakymo eiluciu
    data = models.DateField(_('Order date'), default=date.today, null=False)
    automobilis_id = models.ForeignKey('Automobilis', verbose_name=_('Information'),
                                       on_delete=models.CASCADE, null=False, related_name='auto_statusas')

    UZSAKYMO_STATUSAS = (
        ('l', _('Waiting for car')),
        ('a', _('Car under maintenance')),
        ('u', _('Order completed')),
        ('x', _('Order cancelled')),
    )

    statusas = models.CharField(max_length=1, choices=UZSAKYMO_STATUSAS, default='l', null=False, help_text=_('Status'))
    vartotojas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    grazinimo_terminas = models.DateField(_('Order completion date'), null=True, blank=True)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'{self.data}: {self.automobilis_id}.'

    @property
    def is_viso(self):
        # suskaiciuoju visu eiluciu uzsakymu suma
        self.suma = 0
        for eilute in self.uzsakymoeilute_set.all():
            self.suma += eilute.viso_eilute
        return self.suma

    @property
    def is_overdue(self):
        if self.grazinimo_terminas and date.today() > self.grazinimo_terminas:
            return True
        return False


class UzsakymoEilute(models.Model):
    # viena eilute viena paslauga
    paslauga_id = models.ForeignKey('Paslauga', verbose_name=_('Service'), on_delete=models.CASCADE, null=False)
    uzsakymas_id = models.ForeignKey('Uzsakymas', verbose_name=_('Order information'), on_delete=models.CASCADE,
                                     null=False)
    kiekis = models.IntegerField(null=False, help_text=_('Enter amount'))

    class Meta:
        verbose_name = _('Order line')
        verbose_name_plural = _('Order lines')

    def __str__(self):
        return f'{self.paslauga_id} - {self.uzsakymas_id} - {self.kiekis} '

    @property
    def viso_eilute(self):
        # suskaiciuoju eilutes suma
        self.eilutes_suma = self.kiekis * self.paslauga_id.kaina
        return self.eilutes_suma


class Paslauga(models.Model):
    # paslaugos pavadinimas ir kaina
    pavadinimas = models.CharField(_('Service name'), max_length=200, null=False, unique=True,
                                   help_text=_('Enter name of the service'))
    kaina = models.FloatField(_('Price'), max_length=10, null=False, help_text=_('Enter price'))

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return {self.pavadinimas}


class UzsakymasReview(models.Model):
    uzsakymas_review_id = models.ForeignKey('Uzsakymas', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    atsiliepimo_tekstas = models.TextField(_('Comment'), max_length=2000)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['-date_created']


class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def __str__(self):
        return {self.user.username}

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)
