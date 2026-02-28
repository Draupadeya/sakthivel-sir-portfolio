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
                'google_scholar_citations': '239',
                'h_index': '8',
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
                    'degree': 'M.B.A',
                    'institution': 'Alagappa University',
                    'year': '2024',
                    'specialization': 'Education Management',
                    'order': 1
                },
                {
                    'degree': 'Ph.D.',
                    'institution': 'Kalasalingam Academy of Research and Education, Krishnankoil',
                    'year': '2022',
                    'specialization': 'Biomechanics, Biocomposite and Instrumentation',
                    'order': 2
                },
                {
                    'degree': 'M.Tech',
                    'institution': 'Vellore Institute of Technology, Vellore',
                    'year': '2015',
                    'specialization': 'Biomedical Engineering',
                    'order': 3
                },
                {
                    'degree': 'B.E',
                    'institution': 'Adhiparasakthi Engineering College, Melmaruvathur',
                    'year': '2013',
                    'specialization': 'Electronics and Communication Engineering',
                    'order': 4
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
                institution='Kalasalingam Academy of Research and Education, Krishnankoil',
                from_date='15-06-2023 - Present',
                description='Responsible for teaching Biomedical and Electronics subjects, laboratory practices, acting as placement and training coordinator, Internship coordinator, and class advisor. Administrative roles include Industry-Institute Interaction, Valuation Centre In-Charge, and IQAC Coordinator.',
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
                    'institution': 'SRM Institute of Science and Technology, Ramapuram',
                    'from_date': '25-07-2022',
                    'to_date': '25-05-2023',
                    'description': 'Department of Biomedical Engineering',
                    'order': 1
                },
                {
                    'position': 'Assistant Professor',
                    'institution': 'Saveetha Engineering College',
                    'from_date': '18-03-2022',
                    'to_date': '09-07-2022',
                    'description': 'Department of Biomedical Engineering',
                    'order': 2
                },
                {
                    'position': 'Assistant Professor',
                    'institution': 'Kalasalingam Academy of Research and Education, Krishnankoil',
                    'from_date': '20-12-2016',
                    'to_date': '17-03-2022',
                    'description': 'Department of Biomedical Engineering - Teaching and research responsibilities',
                    'order': 3
                },
                {
                    'position': 'Summer Faculty Research Fellow',
                    'institution': 'Indian Institute of Technology, New Delhi',
                    'from_date': '2018',
                    'to_date': '2018',
                    'description': 'Under guidance of Prof. Sitikantha Roy, Department of Applied Mechanics (2 months)',
                    'order': 4
                },
                {
                    'position': 'Assistant Professor',
                    'institution': 'Rajiv Gandhi College of Engineering and Technology, Pondicherry',
                    'from_date': '06-07-2015',
                    'to_date': '18-12-2016',
                    'description': 'Biomedical Engineering - AICTE approved, Affiliated to Pondicherry University',
                    'order': 5
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
                    'organization': 'Indian Society for Technical Education',
                    'membership_type': 'Life Member',
                    'from_date': '2015',
                    'description': 'LMISTE - Professional member of technical education society',
                    'order': 1
                },
                {
                    'organization': 'Indian Society of Systems for Science and Engineering',
                    'membership_type': 'Life Member',
                    'from_date': '2018',
                    'description': 'LMISSE - Professional member of systems and engineering society',
                    'order': 2
                },
                {
                    'organization': 'Biomedical Engineering Society of India',
                    'membership_type': 'Life Member',
                    'from_date': '2020',
                    'description': 'BMESI - Professional member of biomedical engineering society',
                    'order': 3
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
                    'title': 'Enhancing natural fiber-based polymeric composites with biochar filler particles derived from groundnut shell biomass waste',
                    'authors': 'Sakthivel Sankaran, Geetha Palani, Yo-Lun Yang, Herri Trilaksana',
                    'journal': 'Biomass Conversion and Biorefinery',
                    'year': '2025',
                    'doi': '10.1007/s13399-024-06201-0',
                    'url': '',
                    'order': 1
                },
                {
                    'title': 'Current Trends in Smart Home Sensors for Blood Glucose and Fetal Heart Rate Monitoring: A Systematic Review',
                    'authors': 'S. Sankaran, G. Shivesh, S. Thakur, M. Faizan',
                    'journal': '2025 International Conference on Data Science, Agents & Artificial Intelligence (ICDSAAI)',
                    'year': '2025',
                    'doi': '10.1109/ICDSAAI65575.2025.11011856',
                    'url': '',
                    'order': 2
                },
                {
                    'title': 'Development of artificial intelligence edge computing based wearable device for fall detection and prevention of elderly people',
                    'authors': 'A Paramasivam, M Jenath, TS Sivakumaran, Sakthivel Sankaran, et al.',
                    'journal': 'Heliyon',
                    'year': '2024',
                    'doi': '10.1016/j.heliyon.2024.e31785',
                    'url': '',
                    'order': 3
                },
                {
                    'title': 'Analysis and Optimization of Foot Pressure Patterns in Pes Planus-A Comprehensive Study',
                    'authors': 'S. Sankaran, T. T. Suriya, M. Peerkkanriyash, P. I. Britto',
                    'journal': 'Tenth International Conference on Bio Signals, Images, and Instrumentation (ICBSII)',
                    'year': '2024',
                    'doi': '10.1109/ICBSII61384.2024.10564085',
                    'url': '',
                    'order': 4
                },
                {
                    'title': 'Statistical and Experimental Analysis of the Mechanical Properties of Jute Fiber Reinforced Epoxy Composite for the Transfemoral Prosthesis Biocomposite Socket Applications',
                    'authors': 'Sakthivel Sankaran, Pallikonda Rajasekaran Murugan, ArumugaprabuVeara Simman',
                    'journal': 'Journal of Natural Fibers',
                    'year': '2022',
                    'doi': '10.1080/15440478.2022.2108535',
                    'url': '',
                    'order': 5
                }
            ]
            for pub in pub_data:
                CVPublication.objects.create(**pub)
            self.stdout.write(self.style.SUCCESS('✓ Created sample publication entries'))
        else:
            self.stdout.write(self.style.WARNING('• Publication entries already exist'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ Initial CV data populated!'))
        self.stdout.write(self.style.WARNING('\nYou can now edit all CV data in Django admin at /admin/'))
