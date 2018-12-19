from django.db import models
#from datetime import datetime
from django.utils import timezone
# Create your models here.
class Titolo(models.Model):
    label1 = models.CharField(max_length=100, default='', blank=True)
    label2 = models.CharField(max_length=100, default='', blank=True)
    indirizzo = models.CharField(max_length=100, default='', blank=True)
    telefono = models.CharField(max_length=100, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    sitoweb = models.CharField(max_length=100, default='', blank=True)
    linktwitter = models.CharField(max_length=100, default='', blank=True)
    linkfacebook = models.CharField(max_length=100, default='', blank=True)
    linkinstagram = models.CharField(max_length=100, default='', blank=True)
    class Meta:
            verbose_name="Titolo"
            verbose_name_plural="Titoli"
    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.label2}"

class Testata(models.Model):
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')
    label1 = models.CharField(max_length=100, default='', blank=True)
    label2 = models.CharField(max_length=100, default='', blank=True)
    label3 = models.CharField(max_length=100, default='', blank=True)
    label4 = models.CharField(max_length=100, default='', blank=True)
    testata = models.BooleanField(default=False)
    class Meta:
            verbose_name="Testata"
            verbose_name_plural="Testata"

    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.label2}"

class Presentazione(models.Model):
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')
    label1 = models.CharField(max_length=100, null=True , default='' , blank=True)
    label2 = models.TextField( null=True , default='', blank=True)
    label3 = models.TextField( null=True, default='' , blank=True)
    label4 = models.TextField( null=True, default='' , blank=True)
    videolink = models.CharField(max_length=200, null=True , default='' , blank=True)
    videodescrizione = models.CharField(max_length=400, null=True , default='' , blank=True)
    class Meta:
            verbose_name="Presentazione"
            verbose_name_plural="Presentazione"

    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.label2}"

class Presentazionepunto(models.Model):
    label1 = models.TextField(max_length=400, null=True , default='' , blank=True)
    class Meta:
            verbose_name="Presentazione-punto"
            verbose_name_plural="Presentazione-punti"
    def __str__(self):
        return f"[{self.id}]- {self.label1}"

class Staffdes(models.Model):
    label1 = models.CharField(max_length=100, default='', blank=True)
    label2 = models.CharField(max_length=100, default='', blank=True)
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')

    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.label2}"

class Staff(models.Model):
    nome = models.CharField(max_length=100, null=True, default='' , blank=True)
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')
    label1 = models.CharField(max_length=400, null=True , default='' , blank=True)
    label2 = models.CharField(max_length=400, null=True , default='', blank=True)

    def __str__(self):
        return f"[{self.id}]- {self.nome} -->{self.label2}"

class Blogdes(models.Model):
    label1 = models.CharField(max_length=100, default='', blank=True)
    label2 = models.CharField(max_length=100, default='', blank=True)
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')
    class Meta:
            verbose_name_plural="Blog-descrizione"
    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.label2}"

class Blog(models.Model):
    nome = models.CharField(max_length=100, null=True, default='' , blank=True)
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')
    label1 = models.CharField(max_length=400, null=True , default='' , blank=True)
    label2 = models.CharField(max_length=400, null=True , default='', blank=True)
    link = models.CharField(max_length=400, null=True , default='', blank=True)

    def __str__(self):
        return f"[{self.id}]- {self.nome} -->{self.label1}"

class Footeradv(models.Model):
    label1 = models.CharField(max_length=100, default='', blank=True)
    label2 = models.CharField(max_length=100, default='', blank=True)
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')
    class Meta:
            verbose_name_plural="Footer-adv"
    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.label2}"

class Servizi(models.Model):
    flaticon_name = models.CharField(max_length=100, default='', blank=True)
    label1 = models.TextField( default='', blank=True)
    testo1 = models.TextField( default='', blank=True)
    testo2 = models.TextField( default='', blank=True)
    testo3 = models.TextField( default='', blank=True)
    testo4 = models.TextField( default='', blank=True)
    testo5 = models.TextField( default='', blank=True)

    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.testo1}"

class Servizides(models.Model):
    label1 = models.CharField(max_length=100, default='', blank=True)
    label2 = models.CharField(max_length=100, default='', blank=True)
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')

    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.label2}"

class Contatto(models.Model):
    label1 = models.CharField(max_length=100, default='', blank=True)
    label2 = models.CharField(max_length=100, default='', blank=True)
    image  = models.ImageField(null=True, blank=True, upload_to = 'static/media/')

    def __str__(self):
        return f"[{self.id}]- {self.label1} -->{self.label2}"

class Contattorichiesta(models.Model):
    nome = models.CharField(max_length=100, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    soggetto = models.CharField(max_length=200, default='', blank=True)
    oggetto = models.TextField( default='', blank=True)
    datarichiesta = models.DateTimeField(default=timezone.now )

    def __str__(self):
        return f"[{self.id}]- {self.email} -->{self.soggetto}"
