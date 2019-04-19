from django.urls import path
from .views import FiltroBoostrapView


urlpatterns = [
    path('', FiltroBoostrapView, name='bootstrapview'),
]

