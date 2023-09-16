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

# Query all courses
#############################WRITE ALL YOUR QUERIES BELOW#################################
