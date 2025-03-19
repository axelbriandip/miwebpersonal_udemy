from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    description = models.TextField(verbose_name="descripción")
    image = models.ImageField(verbose_name="imágen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="últ. fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ['-created']

    def __str__(self):
        return self.title