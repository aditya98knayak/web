from django.urls import path
from .views import mem_details, joinF, join, remove, removeF, audi_booking, audi, remove_audi, user_update

app_name = 'Member'

urlpatterns = [
    path('details', mem_details, name='Mdetails'),
    path('joinF', joinF, name='joinF'),
    path('join/<int:slugid>/<int:slugdays>', join, name='join'),
    path('removeF', removeF, name='removeF'),
    path('remove/<int:slug>', remove, name='remove'),
    path('auditorium', audi, name='audi'),
    path('book', audi_booking, name='audi_booking'),
    path('removeA/<int:slug>', remove_audi, name='removeA'),
    path('edit/', user_update, name='edit'),
]
