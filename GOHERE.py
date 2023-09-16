import os
import warnings
from flask import Flask
from app.factory import create_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Course, Enrollment, Student
warnings.simplefilter('ignore', category=Warning, append=True)
app = create_app()
database_path = os.path.join(app.instance_path, 'dev.db')
engine = create_engine(f'sqlite:///{database_path}')
Session = sessionmaker(bind=engine)
session = Session()

##SETUP:  CREATE A VIRTUAL ENVIRO.  ENTER IT.  THEN pip install -r requirements.txt

# Query all courses
#############################WRITE ALL YOUR QUERIES BELOW#################################

#get all students


allStudents=1

print(allStudents) #[<Student 1>, <Student 2>, <Student 3>, <Student 4>, <Student 5>, <Student 6>, <Student 7>, <Student 8>, <Student 9>, <Student 10>, <Student 11>, <Student 12>, <Student 13>, <Student 14>, <Student 15>, <Student 16>, <Student 17>, <Student 18>, <Student 19>, <Student 20>]

#get student by primary key of 4

numberFour=1
print(numberFour)   #<Student 4>


# get all of the students, but just their names

all_names=1
print(all_names)   #[('Kenneth Blake',), ('Patrick Rodriguez',), ('Miss Kimberly Mckinney',), ('Denise Martinez',), ('Frank Mooney',), ('Anita Lewis',), ('Lindsay Smith',), ('Steven Daniels',), ('Sabrina Henry',), ('Mark Cruz',), ('Emily Bray',), ('Stacie White',), ('Edward Fritz',), ('Karen Jones',), ('Cynthia Cook',), ('Melanie Joseph',), ('Erin Booth',), ('Melissa Spears',), ('Michael Fitzgerald',), ('Diana Turner',)]

#get all of students names, order by names

ordered_names=1
print('ordered names',ordered_names)  #ordered names [('Anita Lewis',), ('Cynthia Cook',), ('Denise Martinez',), ('Diana Turner',), ('Edward Fritz',), ('Emily Bray',), ('Erin Booth',), ('Frank Mooney',), ('Karen Jones',), ('Kenneth Blake',), ('Lindsay Smith',), ('Mark Cruz',), ('Melanie Joseph',), ('Melissa Spears',), ('Michael Fitzgerald',), ('Miss Kimberly Mckinney',), ('Patrick Rodriguez',), ('Sabrina Henry',), ('Stacie White',), ('Steven Daniels',)]

#use filter to only get names with a length above 5
namesAbove5=1

print(namesAbove5)


#COUNT HOW MANY STUDENTS THERE ARE

countOfStudents=1

print(countOfStudents)
