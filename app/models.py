from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Define a many-to-many relationship with courses through the 'enrollments' association table
    courses = db.relationship('Course', secondary='enrollments', back_populates='students')

    enrollments = db.relationship('Enrollment', back_populates='student')  # Add this line

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    # Define a many-to-many relationship with students through the 'enrollments' association table
    students = db.relationship('Student', secondary='enrollments', back_populates='courses')

    enrollments = db.relationship('Enrollment', back_populates='course')  # Add this line

class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')
