from django.db import models

# Create your models here.


class Facility(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=90)
    thumbnail = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.thumbnail.delete()
        super().delete()
