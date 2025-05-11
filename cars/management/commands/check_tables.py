from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Check database tables'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            self.stdout.write(f"Tables: {tables}")