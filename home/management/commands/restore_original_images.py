from django.core.management.base import BaseCommand
from home.models import Award, GalleryImage


class Command(BaseCommand):
    help = 'Restore original award and gallery images from Supabase Storage'

    def handle(self, *args, **options):
        """Restore original awards and gallery images"""
        
        # Clear existing records
        Award.objects.all().delete()
        GalleryImage.objects.all().delete()
        
        self.stdout.write(self.style.WARNING('Cleared existing records'))
        
        # Restore Awards
        award_data = [
            {
                'title': 'Best Departmental Contribution',
                'organization': 'Department',
                'description': 'Award for outstanding departmental contribution',
                'certificate': 'awards/bd_1.png'
            },
            {
                'title': 'Faculty Award',
                'organization': 'Faculty',
                'description': 'Award for faculty excellence',
                'certificate': 'awards/FA.png'
            }
        ]
        
        for data in award_data:
            award = Award.objects.create(**data)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Restored award: {award.title}')
            )
        
        # Restore Gallery Images
        gallery_data = [
            {
                'title': 'Fellowship',
                'description': 'Fellowship award image',
                'image': 'gallery/fellowship.png',
                'order': 1
            },
            {
                'title': 'Gallery Image',
                'description': 'Gallery showcase image',
                'image': 'gallery/G1.png',
                'order': 2
            }
        ]
        
        for data in gallery_data:
            img = GalleryImage.objects.create(**data)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Restored gallery: {img.title}')
            )
        
        self.stdout.write(
            self.style.SUCCESS('\n✓ Original images restored from Supabase Storage')
        )
