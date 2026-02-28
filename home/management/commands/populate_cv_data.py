from django.core.management.base import BaseCommand
from home.models import CVStatistics, CVEducation, CVCurrentPosition, CVExperience, CVProfessionalMembership, CVPublication


class Command(BaseCommand):
    help = 'Populate initial CV data for editing in Django admin'

    def handle(self, *args, **options):
        """Create initial CV data if it doesn't exist"""
        
        # Create or update CV Statistics
        stats, created = CVStatistics.objects.get_or_create(
            pk=1,
            defaults={
                'google_scholar_citations': '239+',
                'h_index': 'H-8',
                'publications': '50+',
                'patents': '9+'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created CV Statistics'))
        else:
            self.stdout.write(self.style.WARNING('• CV Statistics already exists'))
        
        # Create sample education entries if none exist
        if not CVEducation.objects.exists():
            edu_data = [
                {
                    'degree': 'Ph.D.',
                    'institution': 'University Name',
                    'year': '2015',
                    'specialization': 'Your Specialization',
                    'order': 1
                },
                {
                    'degree': 'Master\'s',
                    'institution': 'University Name',
                    'year': '2010',
                    'specialization': 'Your Specialization',
                    'order': 2
                },
                {
                    'degree': 'Bachelor\'s',
                    'institution': 'University Name',
                    'year': '2008',
                    'specialization': 'Your Specialization',
                    'order': 3
                }
            ]
            for edu in edu_data:
                CVEducation.objects.create(**edu)
            self.stdout.write(self.style.SUCCESS('✓ Created sample education entries'))
        else:
            self.stdout.write(self.style.WARNING('• Education entries already exist'))
        
        # Create sample current position if none exist
        if not CVCurrentPosition.objects.exists():
            CVCurrentPosition.objects.create(
                title='Associate Professor',
                department='Department of Biomedical Engineering',
                institution='Kalasalingam Academy of Research and Education',
                from_date='2018 - Present',
                description='Teaching and research in biomedical engineering',
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created current position'))
        else:
            self.stdout.write(self.style.WARNING('• Current position already exists'))
        
        # Create sample experience entries if none exist
        if not CVExperience.objects.exists():
            exp_data = [
                {
                    'position': 'Assistant Professor',
                    'institution': 'Kalasalingam Academy of Research and Education',
                    'from_date': '2015',
                    'to_date': '2018',
                    'description': 'Teaching and research responsibilities',
                    'order': 1
                },
                {
                    'position': 'Post-Doctoral Researcher',
                    'institution': 'Research Institution',
                    'from_date': '2013',
                    'to_date': '2015',
                    'description': 'Research and publication work',
                    'order': 2
                }
            ]
            for exp in exp_data:
                CVExperience.objects.create(**exp)
            self.stdout.write(self.style.SUCCESS('✓ Created sample experience entries'))
        else:
            self.stdout.write(self.style.WARNING('• Experience entries already exist'))
        
        # Create sample memberships if none exist
        if not CVProfessionalMembership.objects.exists():
            mem_data = [
                {
                    'organization': 'IEEE',
                    'membership_type': 'Member',
                    'from_date': '2010',
                    'description': 'Professional member',
                    'order': 1
                },
                {
                    'organization': 'Professional Organization',
                    'membership_type': 'Fellow',
                    'from_date': '2015',
                    'description': '',
                    'order': 2
                }
            ]
            for mem in mem_data:
                CVProfessionalMembership.objects.create(**mem)
            self.stdout.write(self.style.SUCCESS('✓ Created sample membership entries'))
        else:
            self.stdout.write(self.style.WARNING('• Membership entries already exist'))
        
        # Create sample publications if none exist
        if not CVPublication.objects.exists():
            pub_data = [
                {
                    'title': 'Sample Research Paper Title',
                    'authors': 'Author Name, Co-Author Name',
                    'journal': 'Journal Name',
                    'year': '2023',
                    'doi': '10.xxxx/xxxxx',
                    'url': 'https://example.com',
                    'order': 1
                },
                {
                    'title': 'Another Research Paper',
                    'authors': 'Author Name, Co-Author Name',
                    'journal': 'Another Journal',
                    'year': '2022',
                    'doi': '10.xxxx/xxxxx',
                    'url': 'https://example.com',
                    'order': 2
                }
            ]
            for pub in pub_data:
                CVPublication.objects.create(**pub)
            self.stdout.write(self.style.SUCCESS('✓ Created sample publication entries'))
        else:
            self.stdout.write(self.style.WARNING('• Publication entries already exist'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ Initial CV data populated!'))
        self.stdout.write(self.style.WARNING('\nYou can now edit all CV data in Django admin at /admin/'))
