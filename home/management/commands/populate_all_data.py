from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Populate all initial data for the portfolio'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Populating all portfolio data...\n'))
        
        commands = [
            'populate_profile',
            'populate_cv_data',
            'populate_achievements',
            'populate_patents',
        ]
        
        for cmd in commands:
            try:
                call_command(cmd)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error running {cmd}: {e}'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ All data populated successfully!'))
        self.stdout.write(self.style.WARNING('You can now edit data in Django admin at /admin/'))
