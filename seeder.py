import os
from dotenv import load_dotenv
from app.factory import create_app, db
from app.models import Student, Course, Enrollment
from faker import Faker
import random

# Load environment variables from .env
load_dotenv()

# Create a Flask app context
app = create_app()

# Initialize Faker to generate realistic data
fake = Faker()

# Define a list of common university courses
sample_courses = [
    "Philosophy",
    "Computer Science",
    "Psychology",
    "Biology",
    "History",
    "Mathematics",
    "Economics",
    "Physics",
    "Chemistry",
    "English Literature",
    "Political Science",
    "Sociology",
    "Art History",
    "Engineering",
    "Geology",
    "Music",
    "Foreign Languages",
    "Theater",
    "Education",
]

def seed_database():
    with app.app_context():
        # Create students with random human names
        students = [Student(name=fake.name()) for _ in range(20)]
        db.session.add_all(students)

        # Create university courses
        courses = [Course(title=course) for course in sample_courses]
        db.session.add_all(courses)

        # Enroll students in random courses
        for student in students:
            num_enrollments = random.randint(1, 5)  # Enroll each student in 1 to 5 courses
            random_courses = random.sample(courses, num_enrollments)
            for course in random_courses:
                enrollment = Enrollment(student=student, course=course)
                db.session.add(enrollment)

        db.session.commit()

if __name__ == "__main__":
    seed_database()
