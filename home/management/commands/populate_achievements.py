from django.core.management.base import BaseCommand
from home.models import Achievement


class Command(BaseCommand):
    help = 'Populate initial achievement data'

    def handle(self, *args, **options):
        if not Achievement.objects.exists():
            achievements = [
                {
                    'title': 'International Travel Grant - ANRF Young Scientists',
                    'description': 'Awarded 1.91 lakhs rupees by Government of India to present research at ICST2024, Sydney, Australia',
                    'date': '2024-01-15'
                },
                {
                    'title': 'Teaching Competency Award',
                    'description': 'IQAC, Kalasalingam Academy of Research and Education for effective implementation of Problem and Project-Based Learning (PBL) in Sensors and Data Acquisition course',
                    'date': '2024-12-01'
                },
                {
                    'title': 'Mentorship Award',
                    'description': 'IQAC, Kalasalingam Academy of Research and Education for successfully guiding students in hackathon events',
                    'date': '2024-12-01'
                },
                {
                    'title': 'Young Scientist Award',
                    'description': 'VD Good Technology Factory Recognition for young scientific researchers',
                    'date': '2021-07-16'
                },
                {
                    'title': 'Teaching Competence Award',
                    'description': 'Kalasalingam Academy of Research and Education for academic year 2018-2019',
                    'date': '2020-01-15'
                },
                {
                    'title': 'Best UG Major Project Award',
                    'description': 'Kalasalingam Academy of Research and Education for guiding outstanding undergraduate projects',
                    'date': '2020-01-15'
                },
                {
                    'title': 'Competence Award for Faculty Advisorship',
                    'description': 'Kalasalingam Academy of Research and Education for exceptional faculty mentorship',
                    'date': '2018-10-15'
                },
                {
                    'title': 'Fellowship Award - IIT Delhi',
                    'description': 'Summer Faculty Research Fellowship - Motivational Award for prestigious fellowship at Indian Institute of Technology, New Delhi',
                    'date': '2018-10-15'
                },
                {
                    'title': 'IEDC Project Award',
                    'description': 'Motivational Award for Innovation and Entrepreneurship Development Centre Project',
                    'date': '2018-08-15'
                },
                {
                    'title': 'Best Motivator Award',
                    'description': 'Regional Blood Transfusion Centre, Meenakshi Mission Hospital and Research Centre, Madurai for voluntarily involving in Blood donation camp under NSS',
                    'date': '2017-03-15'
                },
                {
                    'title': 'University Level NSS Award',
                    'description': 'Kalasalingam Academy of Research and Education for National Service Scheme contributions',
                    'date': '2017-10-15'
                },
                {
                    'title': 'Best Paper Award at SET 2014',
                    'description': '8th International Conference on Science, Engineering and Technology at VIT University for paper on "Heating Gloves for Hypothermia Treatment"',
                    'date': '2014-05-06'
                }
            ]
            for ach in achievements:
                Achievement.objects.create(**ach)
            self.stdout.write(self.style.SUCCESS('✓ Created sample achievements'))
        else:
            self.stdout.write(self.style.WARNING('• Achievements already exist'))
