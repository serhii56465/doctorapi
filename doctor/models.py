from django.db import models
from django.template.defaultfilters import slugify


class Area(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    areas = models.ManyToManyField(Area, blank=True)
    description = models.TextField()
    birthday = models.DateField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["id", "name"]
