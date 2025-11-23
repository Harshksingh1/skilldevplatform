"""
Management command to create sample skills with categories
"""
from django.core.management.base import BaseCommand
from skills.models import Skill, SkillCategory


class Command(BaseCommand):
    help = 'Creates sample skills with categories'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample skills...'))

        # Create or get categories
        categories_data = [
            {'name': 'Technology', 'description': 'Technology and software development skills', 'icon': 'fas fa-laptop-code'},
            {'name': 'Business', 'description': 'Business and management skills', 'icon': 'fas fa-briefcase'},
            {'name': 'Design', 'description': 'Design and creative skills', 'icon': 'fas fa-palette'},
            {'name': 'Data Science', 'description': 'Data analysis and science skills', 'icon': 'fas fa-chart-bar'},
            {'name': 'Marketing', 'description': 'Marketing and communication skills', 'icon': 'fas fa-bullhorn'},
            {'name': 'Soft Skills', 'description': 'Personal and interpersonal skills', 'icon': 'fas fa-users'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = SkillCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'icon': cat_data['icon'],
                    'is_active': True
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        # Skills data
        skills_data = [
            # Technology Skills
            {
                'name': 'Python Programming',
                'description': 'Master Python programming language for web development, data science, and automation.',
                'category': 'Technology',
                'difficulty': 'intermediate',
                'duration': 80,
            },
            {
                'name': 'JavaScript Development',
                'description': 'Learn JavaScript for frontend and backend development with modern frameworks.',
                'category': 'Technology',
                'difficulty': 'intermediate',
                'duration': 70,
            },
            {
                'name': 'Full Stack Development',
                'description': 'Complete full-stack web development skills including frontend and backend technologies.',
                'category': 'Technology',
                'difficulty': 'advanced',
                'duration': 120,
            },
            {
                'name': 'Cloud Computing (AWS)',
                'description': 'Amazon Web Services cloud computing platform skills for scalable applications.',
                'category': 'Technology',
                'difficulty': 'advanced',
                'duration': 100,
            },
            {
                'name': 'DevOps & Docker',
                'description': 'DevOps practices, containerization with Docker, and CI/CD pipeline management.',
                'category': 'Technology',
                'difficulty': 'advanced',
                'duration': 90,
            },
            # Business Skills
            {
                'name': 'Project Management',
                'description': 'Effective project planning, execution, and management methodologies.',
                'category': 'Business',
                'difficulty': 'intermediate',
                'duration': 60,
            },
            {
                'name': 'Business Analytics',
                'description': 'Data-driven decision making using analytics tools and techniques.',
                'category': 'Business',
                'difficulty': 'intermediate',
                'duration': 70,
            },
            {
                'name': 'Strategic Planning',
                'description': 'Strategic thinking and long-term business planning skills.',
                'category': 'Business',
                'difficulty': 'advanced',
                'duration': 50,
            },
            # Design Skills
            {
                'name': 'UI/UX Design',
                'description': 'User interface and user experience design principles and practices.',
                'category': 'Design',
                'difficulty': 'intermediate',
                'duration': 80,
            },
            {
                'name': 'Graphic Design',
                'description': 'Visual design, typography, color theory, and branding design skills.',
                'category': 'Design',
                'difficulty': 'intermediate',
                'duration': 75,
            },
            # Data Science Skills
            {
                'name': 'Data Analysis',
                'description': 'Analyzing data using statistical methods and data visualization tools.',
                'category': 'Data Science',
                'difficulty': 'intermediate',
                'duration': 65,
            },
            {
                'name': 'Machine Learning',
                'description': 'Machine learning algorithms, neural networks, and AI model development.',
                'category': 'Data Science',
                'difficulty': 'advanced',
                'duration': 100,
            },
            # Marketing Skills
            {
                'name': 'Digital Marketing',
                'description': 'SEO, SEM, social media marketing, and online advertising strategies.',
                'category': 'Marketing',
                'difficulty': 'beginner',
                'duration': 50,
            },
            # Soft Skills
            {
                'name': 'Leadership',
                'description': 'Leadership principles, team management, and inspiring others.',
                'category': 'Soft Skills',
                'difficulty': 'intermediate',
                'duration': 40,
            },
            {
                'name': 'Communication Skills',
                'description': 'Effective verbal and written communication for professional settings.',
                'category': 'Soft Skills',
                'difficulty': 'beginner',
                'duration': 35,
            },
        ]

        created_count = 0
        for skill_data in skills_data:
            # Check if skill already exists
            if Skill.objects.filter(name=skill_data['name']).exists():
                self.stdout.write(self.style.WARNING(f'Skill "{skill_data["name"]}" already exists, skipping...'))
                continue

            category = categories.get(skill_data['category'])
            if not category:
                self.stdout.write(self.style.ERROR(f'Category "{skill_data["category"]}" not found, skipping skill "{skill_data["name"]}"'))
                continue

            skill = Skill.objects.create(
                name=skill_data['name'],
                description=skill_data['description'],
                category=category,
                difficulty_level=skill_data['difficulty'],
                estimated_duration_hours=skill_data['duration'],
                is_active=True,
            )

            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'Created skill: {skill.name}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} skills!'))

