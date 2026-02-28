from django.core.management.base import BaseCommand
from home.models import CVPatent


class Command(BaseCommand):
    help = 'Populate initial patent data'

    def handle(self, *args, **options):
        if not CVPatent.objects.exists():
            patents = [
                {
                    'title': 'Patent Title 1',
                    'patent_number': 'US 12345678',
                    'filing_date': '2022-01-15',
                    'status': 'granted',
                    'description': 'Patent description here'
                },
                {
                    'title': 'Patent Title 2',
                    'patent_number': 'US 87654321',
                    'filing_date': '2021-06-10',
                    'status': 'granted',
                    'description': 'Another patent description'
                }
            ]
            for patent in patents:
                CVPatent.objects.create(**patent)
            self.stdout.write(self.style.SUCCESS('✓ Created sample patents'))
        else:
            self.stdout.write(self.style.WARNING('• Patents already exist'))
