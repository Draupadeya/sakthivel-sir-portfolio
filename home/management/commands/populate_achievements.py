from django.core.management.base import BaseCommand
from home.models import Achievement


class Command(BaseCommand):
    help = 'Populate initial achievement data'

    def handle(self, *args, **options):
        if not Achievement.objects.exists():
            achievements = [
                {
                    'title': 'Google Scholar Citations: 239+',
                    'description': 'Over 239+ research citations on Google Scholar, demonstrating significant research impact and contribution to scientific knowledge',
                    'date': '2025-03-01'
                },
                {
                    'title': 'H-Index: 8',
                    'description': 'H-Index of 8 demonstrating consistent productivity and high citation impact in research publications',
                    'date': '2025-03-01'
                },
                {
                    'title': '50+ Publications',
                    'description': 'Published over 50 research papers including SCI-indexed journals (IF up to 5.2), SCOPUS-indexed, and IEEE conferences',
                    'date': '2025-03-01'
                },
                {
                    'title': '9+ Patents Filed',
                    'description': 'Filed 9+ patents including 1 granted and 8 under review in biomedical technologies and wearable devices',
                    'date': '2025-03-01'
                },
                {
                    'title': 'Funded Projects: 2.23 Lakhs EDII',
                    'description': 'Successfully guided student team to secure 2.23 Lakhs rupees through EDII-Innovation Voucher Programme for innovation development',
                    'date': '2018-01-15'
                },
                {
                    'title': 'DST-IEDC Project: 1 Lakh',
                    'description': 'Guided students and secured 1 Lakh rupees funding through DST-Innovation and Entrepreneurship Development Centre project',
                    'date': '2018-06-15'
                },
                {
                    'title': 'International Travel Research Grant: 1.91 Lakhs',
                    'description': 'Awarded 1.91 lakhs rupees by ANRF (Young Scientists, Govt. of India) for research presentation at ICST2024, Sydney, Australia',
                    'date': '2024-01-15'
                },
                {
                    'title': 'SCI-Indexed Publications',
                    'description': 'Published in peer-reviewed SCI-indexed journals with high impact factors (IF 3.5-5.2) including Biomass Conversion and Biorefinery, Heliyon, IEEE Transactions',
                    'date': '2024-12-01'
                },
                {
                    'title': '100% Student Pass Rate',
                    'description': 'Consistently achieved 100% passed out results by implementing moral discipline and regular study habits in Biomedical and Electronics Engineering courses',
                    'date': '2024-12-01'
                },
                {
                    'title': 'Multiple Co-Authored Publications',
                    'description': 'Co-authored 30+ research papers with international and national collaborators demonstrating strong interdisciplinary research collaboration',
                    'date': '2024-12-01'
                },
                {
                    'title': 'Journal Reviewer',
                    'description': 'Serving as peer reviewer for 4+ international journals: Journal of Engineering Education Transformations, Journal of Pharmaceutical Research International, BioMed Research International, Computers in Biology and Medicine',
                    'date': '2024-12-01'
                },
                {
                    'title': 'Online Certifications',
                    'description': 'Successfully completed NPTEL Online Course on "Biomedical Nanotechnology" and AutoCAD certification demonstrating commitment to continuous learning',
                    'date': '2017-11-04'
                }
            ]
            for ach in achievements:
                Achievement.objects.create(**ach)
            self.stdout.write(self.style.SUCCESS('✓ Created sample achievements'))
        else:
            self.stdout.write(self.style.WARNING('• Achievements already exist'))
