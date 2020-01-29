from django.contrib import admin
from .models import FacilityChosen, Auditorium, Membership

# Register your models here.
admin.site.register(FacilityChosen)
admin.site.register(Auditorium)
admin.site.register(Membership)
