🌟 SkillDev – Online Learning Management System (LMS)
SkillDev is a simple and user-friendly Learning Management System built using Django. It allows users to explore courses, search educators, browse skills, and enroll in learning programs easily. Administrators have full control to manage courses, skills, educators, and uploaded content. SkillDev aims to make online learning smooth, accessible, and well-organized for everyone.

🚀 Features
👨‍🎓 For Learners
User Login & Registration

Browse all courses with clean categorization

Apply filters to find the right course

Search and view educator profiles

Explore skill categories

Enroll in courses

Access uploaded videos, documents, and study materials

🛠️ For Admin
Add/Edit/Delete Courses

Add/Edit/Delete Educators

Add/Edit/Delete Skills

Upload & manage learning content

Manage users and enrollments

🏗️ Tech Stack
Section	Technology
Backend	Django (Python)
Frontend	HTML, CSS, JavaScript
Database	SQLite / MySQL
Authentication	Django Auth
 
1. Clone the Repository
git clone https://github.com/Harshksingh1/skilldevplatform.git
cd skilldev
2. Create a Virtual Environment
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
5. Create Superuser (Admin Login)
python manage.py createsuperuser
6. Run the Development Server
python manage.py runserver
Your app will run at:
👉 http://127.0.0.1:8000/

🧩 Modules
🔹 User Module
Register / Login

View courses

Enroll in courses

Explore skills

Search educators

🔹 Admin Module
Add skills, courses, educators

Upload course materials
