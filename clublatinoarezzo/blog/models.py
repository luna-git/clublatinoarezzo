from django.db import models
from django.utils import timezone

# Create your models here.

class Image(models.Model):
    immagine = models.ImageField(null=True, blank=True, upload_to = 'static/media/img/')
    label1 = models.CharField(max_length=100, default='', blank=True)
    class Meta:
            verbose_name="Immagine"
            verbose_name_plural="Immagini"

    def __str__(self):
        return f"[{self.id}]- {self.label1} "

class Categoriablog(models.Model):
    categoria = models.CharField(max_length=100, default='', blank=True)
    class Meta:
            verbose_name_plural="Categorie"
            verbose_name="Categoria"

    def __str__(self):
        return f"[{self.id}]- {self.categoria} "

class Articoloblog(models.Model):
    titolo = models.CharField(max_length=300, default='', blank=True)
    sottotitolo = models.TextField( null=True , default='', blank=True)
    testo = models.TextField( null=True , default='', blank=True)
    immagine = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="Fotoblog")
    data = models.DateTimeField(default=timezone.now )
    categoria = models.ForeignKey(Categoriablog, on_delete=models.CASCADE, related_name="Typeart")
    class Meta:
            verbose_name="Articolo"
            verbose_name_plural="Articoli"

    def __str__(self):
        return f"[{self.id}]- {self.titolo} "

class Testatablog(models.Model):
    titolo = models.CharField(max_length=300, default='', blank=True)
    testo = models.TextField( null=True , default='', blank=True)
    immagine = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="Foto")
    class Meta:
            verbose_name="Testata"
            verbose_name_plural="Testata"

    def __str__(self):
        return f"[{self.id}]- {self.titolo} "
