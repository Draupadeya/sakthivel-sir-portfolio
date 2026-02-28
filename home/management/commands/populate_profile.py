from django.core.management.base import BaseCommand
from home.models import ProfileContent


class Command(BaseCommand):
    help = 'Populate initial profile data'

    def handle(self, *args, **options):
        if not ProfileContent.objects.exists():
            career_vision = """I strive to build a distinguished career in a leading engineering institution, driving cutting-edge research and pioneering innovative biomedical technologies. My vision is to bridge engineering and healthcare, developing transformative solutions that enhance lives. With a strong commitment to mentorship, interdisciplinary collaboration, and translational research, I aim to foster scientific innovation and global impact in biomedical engineering."""
            
            ProfileContent.objects.create(
                name='Dr. S. Sakthivel, B.E., M.TECH (BME), Ph.D., MBA',
                title='Associate Professor',
                department='Department of Biomedical Engineering',
                bio=career_vision
            )
            self.stdout.write(self.style.SUCCESS('✓ Created profile'))
        else:
            self.stdout.write(self.style.WARNING('• Profile already exists'))
