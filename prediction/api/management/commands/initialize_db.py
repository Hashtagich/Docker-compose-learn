from django.core.management.base import BaseCommand
from api.models import Prediction


class Command(BaseCommand):
    """Класс для инициализации базы данных из файла predictions.txt."""
    help = '''
    Initialize db with prediction from predictions.txt
    Инициализировать базу данных с предсказанием из predictions.txt'''

    def handle(self, *args, **options):
        if not Prediction.objects.count():
            with open("predictions.txt", "r", encoding='utf-8') as file:
                for prediction in file.readlines():
                    Prediction(text=prediction.replace('\n', '')).save()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
