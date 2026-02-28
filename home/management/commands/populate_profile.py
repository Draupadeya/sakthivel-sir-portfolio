from django.core.management.base import BaseCommand
from home.models import ProfileContent


class Command(BaseCommand):
    help = 'Populate initial profile data'

    def handle(self, *args, **options):
        if not ProfileContent.objects.exists():
            ProfileContent.objects.create(
                name='Dr. S. Sakthivel',
                title='Associate Professor, BME Department',
                department='Biomedical Engineering',
                bio='Passionate educator and researcher in Biomedical Engineering with expertise in sensors and data acquisition systems'
            )
            self.stdout.write(self.style.SUCCESS('✓ Created profile'))
        else:
            self.stdout.write(self.style.WARNING('• Profile already exists'))
