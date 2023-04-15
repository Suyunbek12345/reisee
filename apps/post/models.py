from django.db import models
from django.utils.crypto import get_random_string
from slugify import slugify


class Registration(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    instagram = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    question = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=12, primary_key=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        slug_post = get_random_string(length=12)
        if not self.slug:
            self.slug = slugify(slug_post)
        super().save(*args, **kwargs)


class Work(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=12, primary_key=True, blank=True)
    image = models.ImageField(upload_to='images')
    condition = models.CharField(max_length=1000)
    documents = models.CharField(max_length=1000)
    requirement = models.CharField(max_length=1000
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        slug_post = get_random_string(length=12)
        if not self.slug:
            self.slug = slugify(slug_post)
        super().save(*args, **kwargs)




class WorkImage(models.Model):
    image = models.ImageField(upload_to='images/carousel')
    work = models.ForeignKey(
        to=Work,
        on_delete=models.CASCADE,
        related_name='works'
    )



