from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('club/<int:club_id>/', show_club, name='club'),
]
