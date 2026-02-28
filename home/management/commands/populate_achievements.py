from django.core.management.base import BaseCommand
from home.models import Achievement


class Command(BaseCommand):
    help = 'Populate initial achievement data'

    def handle(self, *args, **options):
        if not Achievement.objects.exists():
            achievements = [
                {
                    'title': 'Best Teaching Award',
                    'description': 'Excellence in teaching and student mentorship',
                    'date': '2023-12-15'
                },
                {
                    'title': 'Research Excellence',
                    'description': 'Outstanding contribution to research',
                    'date': '2023-11-20'
                },
                {
                    'title': 'Innovation Recognition',
                    'description': 'Recognition for innovative projects',
                    'date': '2023-10-10'
                }
            ]
            for ach in achievements:
                Achievement.objects.create(**ach)
            self.stdout.write(self.style.SUCCESS('✓ Created sample achievements'))
        else:
            self.stdout.write(self.style.WARNING('• Achievements already exist'))
