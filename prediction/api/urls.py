from django.urls import path
from.views import PredictionAPIList

urlpatterns = [
    path('predictions/', PredictionAPIList.as_view(), name='predictions'),
]