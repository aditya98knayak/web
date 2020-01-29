from django.db import models
from Web_project.settings import AUTH_USER_MODEL
from Manager_Console.models import Facility
import django.utils.timezone

#Create your models here.


class FacilityChosen(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice = models.ManyToManyField(Facility, through='Membership')

    def __str__(self):
        return str(self.user)
#keeps track of membership model aciltyt chosen and the facility
class Membership(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    choice = models.ForeignKey(FacilityChosen, on_delete=models.CASCADE)
    start_date = models.DateField(default=django.utils.timezone.now)
    end_date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.choice)

class Auditorium(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking_date = models.DateField()
    description = models.TextField(max_length=30)

    def __str__(self):
        return str(self.user)
