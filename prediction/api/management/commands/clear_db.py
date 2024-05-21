from django.core.management.base import BaseCommand
from api.models import Prediction


class Command(BaseCommand):
    """Класс для очистки базы данных."""
    help = 'Clears the database of all predictions.\nОчищает базу данных от всех прогнозов.'

    def handle(self, *args, **options):
        count = Prediction.objects.count()
        Prediction.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи предсказаний в количестве {count} шт. удалены из базы данных.'))
