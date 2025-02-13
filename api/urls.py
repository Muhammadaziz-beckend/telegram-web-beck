from django.urls import path
from apps.authI.views import receive_phone

urlpatterns = [
    path('receive_phone/', receive_phone, name='receive_phone'),
]
