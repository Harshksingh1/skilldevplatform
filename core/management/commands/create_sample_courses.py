"""
Management command to create sample courses with images and details
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from skills.models import Skill, SkillCategory
from training.models import Course, CourseModule
from datetime import timedelta
import random


class Command(BaseCommand):
    help = 'Creates sample courses with images and detailed information'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample courses...'))

        # Get or create instructors
        instructor1, _ = User.objects.get_or_create(
            username='john_doe',
            defaults={
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john.doe@skillsdev.com',
            }
        )
        instructor1.set_password('password123')
        instructor1.save()

        instructor2, _ = User.objects.get_or_create(
            username='jane_smith',
            defaults={
                'first_name': 'Jane',
                'last_name': 'Smith',
                'email': 'jane.smith@skillsdev.com',
            }
        )
        instructor2.set_password('password123')
        instructor2.save()

        instructor3, _ = User.objects.get_or_create(
            username='mike_wilson',
            defaults={
                'first_name': 'Mike',
                'last_name': 'Wilson',
                'email': 'mike.wilson@skillsdev.com',
            }
        )
        instructor3.set_password('password123')
        instructor3.save()

        instructor4, _ = User.objects.get_or_create(
            username='sarah_johnson',
            defaults={
                'first_name': 'Sarah',
                'last_name': 'Johnson',
                'email': 'sarah.johnson@skillsdev.com',
            }
        )
        instructor4.set_password('password123')
        instructor4.save()

        instructors = [instructor1, instructor2, instructor3, instructor4]

        # Get or create categories and skills
        tech_category, _ = SkillCategory.objects.get_or_create(
            name='Technology',
            defaults={'description': 'Technology and software skills', 'icon': 'fas fa-laptop-code'}
        )
        
        business_category, _ = SkillCategory.objects.get_or_create(
            name='Business',
            defaults={'description': 'Business and management skills', 'icon': 'fas fa-briefcase'}
        )

        design_category, _ = SkillCategory.objects.get_or_create(
            name='Design',
            defaults={'description': 'Design and creative skills', 'icon': 'fas fa-palette'}
        )

        data_category, _ = SkillCategory.objects.get_or_create(
            name='Data Science',
            defaults={'description': 'Data analysis and science', 'icon': 'fas fa-chart-bar'}
        )

        # Sample courses with images and details
        courses_data = [
            {
                'title': 'Complete Python Programming Masterclass',
                'description': 'Master Python from beginner to advanced. Learn data structures, algorithms, OOP, web development with Django, and more. Perfect for aspiring developers.',
                'image_url': 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=800',
                'instructor': instructor1,
                'duration_hours': 60,
                'capacity': 50,
                'difficulty': 'intermediate',
                'price': 299.99,
                'category': tech_category,
                'modules': [
                    {'title': 'Python Basics', 'description': 'Introduction to Python syntax and fundamentals', 'duration': 90, 'order': 1},
                    {'title': 'Data Structures', 'description': 'Lists, dictionaries, tuples, and sets', 'duration': 120, 'order': 2},
                    {'title': 'Object-Oriented Programming', 'description': 'Classes, objects, inheritance, and polymorphism', 'duration': 150, 'order': 3},
                    {'title': 'Web Development with Django', 'description': 'Building web applications with Django framework', 'duration': 180, 'order': 4},
                ]
            },
            {
                'title': 'Advanced JavaScript and React Development',
                'description': 'Build modern web applications with React, Redux, and Node.js. Learn hooks, context API, routing, and state management.',
                'image_url': 'https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800',
                'instructor': instructor2,
                'duration_hours': 48,
                'capacity': 40,
                'difficulty': 'advanced',
                'price': 349.99,
                'category': tech_category,
                'modules': [
                    {'title': 'JavaScript ES6+', 'description': 'Modern JavaScript features', 'duration': 90, 'order': 1},
                    {'title': 'React Fundamentals', 'description': 'Components, props, and state', 'duration': 120, 'order': 2},
                    {'title': 'React Hooks & Context', 'description': 'Advanced React patterns', 'duration': 150, 'order': 3},
                    {'title': 'Redux & State Management', 'description': 'Managing complex application state', 'duration': 180, 'order': 4},
                ]
            },
            {
                'title': 'Machine Learning Fundamentals',
                'description': 'Introduction to machine learning algorithms, neural networks, and deep learning. Hands-on projects with real-world datasets.',
                'image_url': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800',
                'instructor': instructor3,
                'duration_hours': 72,
                'capacity': 30,
                'difficulty': 'advanced',
                'price': 449.99,
                'category': data_category,
                'modules': [
                    {'title': 'Introduction to ML', 'description': 'Overview of machine learning concepts', 'duration': 90, 'order': 1},
                    {'title': 'Supervised Learning', 'description': 'Regression and classification algorithms', 'duration': 180, 'order': 2},
                    {'title': 'Neural Networks', 'description': 'Deep learning and neural network architectures', 'duration': 240, 'order': 3},
                    {'title': 'Practical Projects', 'description': 'Real-world ML projects', 'duration': 300, 'order': 4},
                ]
            },
            {
                'title': 'UI/UX Design Mastery',
                'description': 'Learn user interface and user experience design principles. Master design tools like Figma, Adobe XD, and create stunning interfaces.',
                'image_url': 'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800',
                'instructor': instructor4,
                'duration_hours': 54,
                'capacity': 35,
                'difficulty': 'intermediate',
                'price': 399.99,
                'category': design_category,
                'modules': [
                    {'title': 'Design Principles', 'description': 'Fundamentals of good design', 'duration': 90, 'order': 1},
                    {'title': 'User Research', 'description': 'Understanding user needs and behavior', 'duration': 120, 'order': 2},
                    {'title': 'Design Tools', 'description': 'Figma, Adobe XD, and Sketch', 'duration': 180, 'order': 3},
                    {'title': 'Prototyping', 'description': 'Creating interactive prototypes', 'duration': 150, 'order': 4},
                ]
            },
            {
                'title': 'Digital Marketing Strategy',
                'description': 'Comprehensive digital marketing course covering SEO, SEM, social media marketing, email marketing, and analytics.',
                'image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800',
                'instructor': instructor1,
                'duration_hours': 42,
                'capacity': 45,
                'difficulty': 'beginner',
                'price': 249.99,
                'category': business_category,
                'modules': [
                    {'title': 'Marketing Fundamentals', 'description': 'Core marketing concepts', 'duration': 90, 'order': 1},
                    {'title': 'SEO & Content Marketing', 'description': 'Search engine optimization strategies', 'duration': 120, 'order': 2},
                    {'title': 'Social Media Marketing', 'description': 'Social media strategies and campaigns', 'duration': 150, 'order': 3},
                ]
            },
            {
                'title': 'Project Management Professional (PMP)',
                'description': 'Master project management methodologies including Agile, Scrum, and Waterfall. Prepare for PMP certification.',
                'image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800',
                'instructor': instructor2,
                'duration_hours': 56,
                'capacity': 40,
                'difficulty': 'intermediate',
                'price': 549.99,
                'category': business_category,
                'modules': [
                    {'title': 'Project Management Basics', 'description': 'Introduction to PM concepts', 'duration': 120, 'order': 1},
                    {'title': 'Agile Methodology', 'description': 'Agile and Scrum frameworks', 'duration': 180, 'order': 2},
                    {'title': 'Risk Management', 'description': 'Identifying and managing project risks', 'duration': 150, 'order': 3},
                    {'title': 'PMP Exam Preparation', 'description': 'Exam tips and practice tests', 'duration': 120, 'order': 4},
                ]
            },
            {
                'title': 'Data Analysis with SQL and Python',
                'description': 'Learn to extract, analyze, and visualize data using SQL and Python. Master pandas, numpy, and matplotlib for data insights.',
                'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800',
                'instructor': instructor3,
                'duration_hours': 48,
                'capacity': 50,
                'difficulty': 'intermediate',
                'price': 379.99,
                'category': data_category,
                'modules': [
                    {'title': 'SQL Fundamentals', 'description': 'Database queries and joins', 'duration': 120, 'order': 1},
                    {'title': 'Python for Data Analysis', 'description': 'Pandas and NumPy basics', 'duration': 180, 'order': 2},
                    {'title': 'Data Visualization', 'description': 'Creating charts with Matplotlib and Seaborn', 'duration': 150, 'order': 3},
                ]
            },
            {
                'title': 'Full Stack Web Development',
                'description': 'Complete full-stack development course covering HTML, CSS, JavaScript, Node.js, Express, MongoDB, and React.',
                'image_url': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800',
                'instructor': instructor1,
                'duration_hours': 80,
                'capacity': 35,
                'difficulty': 'advanced',
                'price': 599.99,
                'category': tech_category,
                'modules': [
                    {'title': 'Frontend Basics', 'description': 'HTML, CSS, and JavaScript', 'duration': 180, 'order': 1},
                    {'title': 'Backend Development', 'description': 'Node.js and Express.js', 'duration': 240, 'order': 2},
                    {'title': 'Database Integration', 'description': 'MongoDB and database design', 'duration': 180, 'order': 3},
                    {'title': 'Full Stack Project', 'description': 'Building a complete web application', 'duration': 300, 'order': 4},
                ]
            },
            {
                'title': 'Adobe Photoshop & Illustrator Mastery',
                'description': 'Master Adobe Creative Suite. Learn professional design techniques, photo editing, vector graphics, and digital illustration.',
                'image_url': 'https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=800',
                'instructor': instructor4,
                'duration_hours': 50,
                'capacity': 30,
                'difficulty': 'intermediate',
                'price': 349.99,
                'category': design_category,
                'modules': [
                    {'title': 'Photoshop Basics', 'description': 'Interface and basic tools', 'duration': 120, 'order': 1},
                    {'title': 'Advanced Photoshop', 'description': 'Layers, masks, and filters', 'duration': 180, 'order': 2},
                    {'title': 'Illustrator Fundamentals', 'description': 'Vector graphics and drawing', 'duration': 150, 'order': 3},
                ]
            },
            {
                'title': 'Business Analytics & Excel',
                'description': 'Advanced Excel techniques, pivot tables, data modeling, and business intelligence. Make data-driven decisions.',
                'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800',
                'instructor': instructor2,
                'duration_hours': 36,
                'capacity': 60,
                'difficulty': 'beginner',
                'price': 199.99,
                'category': business_category,
                'modules': [
                    {'title': 'Excel Fundamentals', 'description': 'Basic formulas and functions', 'duration': 90, 'order': 1},
                    {'title': 'Advanced Formulas', 'description': 'Complex formulas and arrays', 'duration': 120, 'order': 2},
                    {'title': 'Pivot Tables & Charts', 'description': 'Data analysis with pivot tables', 'duration': 150, 'order': 3},
                ]
            },
            {
                'title': 'Docker & Kubernetes for DevOps',
                'description': 'Learn containerization with Docker and orchestration with Kubernetes. Deploy and scale applications efficiently.',
                'image_url': 'https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=800',
                'instructor': instructor3,
                'duration_hours': 44,
                'capacity': 25,
                'difficulty': 'advanced',
                'price': 449.99,
                'category': tech_category,
                'modules': [
                    {'title': 'Docker Basics', 'description': 'Containers and images', 'duration': 120, 'order': 1},
                    {'title': 'Docker Compose', 'description': 'Multi-container applications', 'duration': 150, 'order': 2},
                    {'title': 'Kubernetes Fundamentals', 'description': 'Pods, services, and deployments', 'duration': 180, 'order': 3},
                ]
            },
            {
                'title': 'Content Writing & Copywriting',
                'description': 'Master the art of writing compelling content. Learn SEO writing, copywriting techniques, and content strategy.',
                'image_url': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800',
                'instructor': instructor4,
                'duration_hours': 40,
                'capacity': 40,
                'difficulty': 'beginner',
                'price': 229.99,
                'category': business_category,
                'modules': [
                    {'title': 'Writing Fundamentals', 'description': 'Grammar and style', 'duration': 90, 'order': 1},
                    {'title': 'SEO Writing', 'description': 'Writing for search engines', 'duration': 120, 'order': 2},
                    {'title': 'Copywriting Techniques', 'description': 'Persuasive writing strategies', 'duration': 150, 'order': 3},
                ]
            },
            {
                'title': 'Cybersecurity Fundamentals',
                'description': 'Learn cybersecurity basics, ethical hacking, network security, and how to protect systems from threats.',
                'image_url': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800',
                'instructor': instructor1,
                'duration_hours': 52,
                'capacity': 30,
                'difficulty': 'intermediate',
                'price': 499.99,
                'category': tech_category,
                'modules': [
                    {'title': 'Security Basics', 'description': 'Introduction to cybersecurity', 'duration': 120, 'order': 1},
                    {'title': 'Network Security', 'description': 'Protecting network infrastructure', 'duration': 180, 'order': 2},
                    {'title': 'Ethical Hacking', 'description': 'Penetration testing basics', 'duration': 150, 'order': 3},
                ]
            },
            {
                'title': 'Graphic Design Masterclass',
                'description': 'Learn graphic design principles, typography, color theory, branding, and create professional designs for print and web.',
                'image_url': 'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800',
                'instructor': instructor4,
                'duration_hours': 58,
                'capacity': 35,
                'difficulty': 'intermediate',
                'price': 399.99,
                'category': design_category,
                'modules': [
                    {'title': 'Design Principles', 'description': 'Fundamentals of graphic design', 'duration': 120, 'order': 1},
                    {'title': 'Typography & Color', 'description': 'Text and color in design', 'duration': 150, 'order': 2},
                    {'title': 'Branding Design', 'description': 'Creating brand identities', 'duration': 180, 'order': 3},
                ]
            },
            {
                'title': 'Cloud Computing with AWS',
                'description': 'Master Amazon Web Services. Learn EC2, S3, Lambda, RDS, and deploy scalable cloud applications.',
                'image_url': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800',
                'instructor': instructor3,
                'duration_hours': 64,
                'capacity': 30,
                'difficulty': 'advanced',
                'price': 599.99,
                'category': tech_category,
                'modules': [
                    {'title': 'AWS Basics', 'description': 'Introduction to AWS services', 'duration': 120, 'order': 1},
                    {'title': 'Compute Services', 'description': 'EC2, Lambda, and containers', 'duration': 180, 'order': 2},
                    {'title': 'Storage & Databases', 'description': 'S3, RDS, and DynamoDB', 'duration': 150, 'order': 3},
                    {'title': 'DevOps on AWS', 'description': 'CI/CD and automation', 'duration': 180, 'order': 4},
                ]
            },
            {
                'title': 'Leadership & Team Management',
                'description': 'Develop leadership skills, learn team management, conflict resolution, and how to inspire and motivate teams.',
                'image_url': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800',
                'instructor': instructor2,
                'duration_hours': 38,
                'capacity': 45,
                'difficulty': 'intermediate',
                'price': 329.99,
                'category': business_category,
                'modules': [
                    {'title': 'Leadership Principles', 'description': 'Core leadership concepts', 'duration': 90, 'order': 1},
                    {'title': 'Team Building', 'description': 'Building effective teams', 'duration': 120, 'order': 2},
                    {'title': 'Conflict Resolution', 'description': 'Managing team conflicts', 'duration': 120, 'order': 3},
                ]
            },
            {
                'title': 'Mobile App Development with Flutter',
                'description': 'Build cross-platform mobile apps with Flutter and Dart. Create beautiful, fast mobile applications for iOS and Android.',
                'image_url': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800',
                'instructor': instructor1,
                'duration_hours': 55,
                'capacity': 35,
                'difficulty': 'intermediate',
                'price': 429.99,
                'category': tech_category,
                'modules': [
                    {'title': 'Flutter Basics', 'description': 'Introduction to Flutter and Dart', 'duration': 120, 'order': 1},
                    {'title': 'UI Development', 'description': 'Building user interfaces', 'duration': 180, 'order': 2},
                    {'title': 'State Management', 'description': 'Managing app state', 'duration': 150, 'order': 3},
                    {'title': 'Publishing Apps', 'description': 'Publishing to app stores', 'duration': 120, 'order': 4},
                ]
            },
            {
                'title': 'Video Editing with Premiere Pro',
                'description': 'Master Adobe Premiere Pro. Learn video editing, color grading, audio mixing, and create professional video content.',
                'image_url': 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800',
                'instructor': instructor4,
                'duration_hours': 46,
                'capacity': 25,
                'difficulty': 'intermediate',
                'price': 379.99,
                'category': design_category,
                'modules': [
                    {'title': 'Premiere Pro Basics', 'description': 'Interface and workflow', 'duration': 120, 'order': 1},
                    {'title': 'Editing Techniques', 'description': 'Advanced editing methods', 'duration': 180, 'order': 2},
                    {'title': 'Color Grading', 'description': 'Professional color correction', 'duration': 150, 'order': 3},
                ]
            },
            {
                'title': 'Data Science with R',
                'description': 'Learn data science using R programming. Statistical analysis, data visualization, and machine learning with R.',
                'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800',
                'instructor': instructor3,
                'duration_hours': 50,
                'capacity': 40,
                'difficulty': 'intermediate',
                'price': 349.99,
                'category': data_category,
                'modules': [
                    {'title': 'R Programming Basics', 'description': 'Introduction to R', 'duration': 120, 'order': 1},
                    {'title': 'Data Manipulation', 'description': 'dplyr and data wrangling', 'duration': 150, 'order': 2},
                    {'title': 'Statistical Analysis', 'description': 'Statistical modeling in R', 'duration': 180, 'order': 3},
                ]
            },
            {
                'title': 'E-commerce & Online Business',
                'description': 'Start and grow your online business. Learn e-commerce platforms, payment processing, marketing, and scaling strategies.',
                'image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800',
                'instructor': instructor2,
                'duration_hours': 43,
                'capacity': 50,
                'difficulty': 'beginner',
                'price': 279.99,
                'category': business_category,
                'modules': [
                    {'title': 'E-commerce Basics', 'description': 'Setting up online stores', 'duration': 120, 'order': 1},
                    {'title': 'Payment & Shipping', 'description': 'Payment gateways and logistics', 'duration': 150, 'order': 2},
                    {'title': 'Marketing & Growth', 'description': 'Growing your online business', 'duration': 120, 'order': 3},
                ]
            },
        ]

        # Create courses
        start_date = timezone.now() + timedelta(days=7)
        created_count = 0

        for course_data in courses_data:
            # Check if course already exists
            if Course.objects.filter(title=course_data['title']).exists():
                self.stdout.write(self.style.WARNING(f'Course "{course_data["title"]}" already exists, skipping...'))
                continue

            # Create course
            course = Course.objects.create(
                title=course_data['title'],
                description=course_data['description'],
                instructor=course_data['instructor'],
                duration_hours=course_data['duration_hours'],
                capacity=course_data['capacity'],
                difficulty_level=course_data['difficulty'],
                price=course_data['price'],
                image_url=course_data.get('image_url', ''),
                start_date=timezone.now() + timedelta(days=random.randint(7, 37)),
                end_date=timezone.now() + timedelta(days=random.randint(38, 68)),
                is_active=True,
            )

            # Create skills for the course if they exist
            category = course_data.get('category')
            if category:
                skills = Skill.objects.filter(category=category)[:3]
                course.skills.set(skills)

            # Create modules
            for module_data in course_data.get('modules', []):
                CourseModule.objects.create(
                    course=course,
                    title=module_data['title'],
                    description=module_data['description'],
                    duration_minutes=module_data['duration'],
                    order=module_data['order'],
                    is_active=True,
                )

            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'Created course: {course.title}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} courses!'))

