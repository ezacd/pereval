from django.urls import path
from .views import *


urlpatterns = [
    path('create/', submit_data, name='submit'),
    path('<int:pk>', get_data, name='get'),
]