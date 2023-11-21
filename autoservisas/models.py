from django.db import models
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField
from PIL import Image

# Create your models here.


class AutomobilioModelis(models.Model):
    # automobilio modelis
    marke = models.CharField('Automobilio markė', max_length=40, null=False, help_text='Įveskite automobilio markę')
    modelis = models.CharField('Automobilio modelis', max_length=40, null=False,
                               help_text='Įveskite automobilio markės modelį')

    class Meta:
        verbose_name = 'Automobilio modelis'
        verbose_name_plural = 'Automobilių modeliai'

    def __str__(self):
        return f'{self.marke} {self.modelis}'


class Automobilis(models.Model):
    # automobilis pagal modeli ir valst.nr+vin+klientas
    valstybinis_nr = models.CharField('Automobilio valstybinis Nr.',
                                      max_length=7, null=False, unique=True, help_text='Įveskite valstybinį numerį')
    automobilio_modelis_id = models.ForeignKey('AutomobilioModelis', verbose_name='Automobilio modelis',
                                               on_delete=models.CASCADE, null=False)
    vin_kodas = models.CharField(max_length=17, null=False, unique=True, help_text='Įveskite automobilio VIN kodą')
    klientas = models.CharField(max_length=100, null=False,
                                help_text='Iveskite klientą (įmonės pavadinimas arba vardas/pavardė)')
    nuotrauka = models.ImageField('Nuotrauka', upload_to='nuotraukos', null=True)
    aprasymas = HTMLField()

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

    def __str__(self):
        return f'{self.valstybinis_nr}, {self.automobilio_modelis_id}, {self.klientas}'


class Uzsakymas(models.Model):
    # uzsakymas kuriame gali buti daug uzsakymo eiluciu
    data = models.DateField('Užsakymo data', default=date.today, null=False)
    automobilis_id = models.ForeignKey('Automobilis', verbose_name='Informacija',
                                       on_delete=models.CASCADE, null=False, related_name='auto_statusas')

    UZSAKYMO_STATUSAS = (
        ('l', 'Laukiama automobilio'),
        ('a', 'Automobilis tvarkomas'),
        ('u', 'Užsakymas atliktas'),
        ('x', 'Užsakymas atšauktas'),
    )

    statusas = models.CharField(max_length=1, choices=UZSAKYMO_STATUSAS, default='l', null=False, help_text='Statusas')
    vartotojas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    grazinimo_terminas = models.DateField('Prognozuojama atlikimo data', null=True, blank=True)

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

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
    paslauga_id = models.ForeignKey('Paslauga', verbose_name='Paslauga', on_delete=models.CASCADE, null=False)
    uzsakymas_id = models.ForeignKey('Uzsakymas', verbose_name='Užsakymo informacija', on_delete=models.CASCADE,
                                     null=False)
    kiekis = models.IntegerField(null=False, help_text="Įveskite kiekį")

    class Meta:
        verbose_name = 'Užsakymo eilutė'
        verbose_name_plural = 'Užsakymo eilutės'

    def __str__(self):
        return f'{self.paslauga_id} - {self.uzsakymas_id} - {self.kiekis} vnt.'

    @property
    def viso_eilute(self):
        # suskaiciuoju eilutes suma
        self.eilutes_suma = self.kiekis * self.paslauga_id.kaina
        return self.eilutes_suma


class Paslauga(models.Model):
    # paslaugos pavadinimas ir kaina
    pavadinimas = models.CharField('Paslaugos pavadinimas', max_length=200, null=False, unique=True,
                                   help_text='Įveskite paslaugos pavadinimą')
    kaina = models.FloatField('Kaina', max_length=10, null=False, help_text='Įveskite paslaugos kainą')

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

    def __str__(self):
        return f'{self.pavadinimas}'


class UzsakymasReview(models.Model):
    uzsakymas_review_id = models.ForeignKey('Uzsakymas', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    atsiliepimo_tekstas = models.TextField('Atsiliepimas', max_length=2000)

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-date_created']


class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    class Meta:
        verbose_name = "Profilis"
        verbose_name_plural = 'Profiliai'

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)
