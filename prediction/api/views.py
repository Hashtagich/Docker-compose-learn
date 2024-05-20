from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, generics

from .models import Prediction
from .serializers import PredictionSerializer


@extend_schema_view(
    get=extend_schema(summary='Предсказание', tags=['Предсказание'])
)
class PredictionAPIList(generics.ListAPIView):
    """
    API для предоставления всех предсказаний.
    """
    serializer_class = PredictionSerializer
    queryset = Prediction.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "data_create",
    ]
