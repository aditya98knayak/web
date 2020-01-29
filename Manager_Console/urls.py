from django.urls import path
from .views import user_view, add_facility, del_facility, remove_Facility, audi

app_name = 'Manager'

urlpatterns = [
    path('UserList', user_view, name='user'),
    path('addFacility', add_facility, name='addf'),
    path('delFacility', del_facility, name='delf'),
    path('removeFacility/<slug:slug>', remove_Facility, name='removef'),
    path('Auditorium', audi, name='audi')
]