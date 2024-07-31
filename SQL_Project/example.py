from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to an in-memory SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)

# Create table - Define a 'Student' table
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(Float)


# Create the table in memory
Base.metadata.create_all(engine)

# INSERT INTO - Insert data into 'Student' table
Session = sessionmaker(bind=engine)
session = Session()

student_a = Student(name='Bahaa', grade=96.6)
student_b = Student(name='Shibel', grade=98.3)

session.add_all([student_a, student_b])
session.commit()

students = session.query(Student).all()

for student in students:
    print(f"{student.name} is on grade {student.grade} and is id {student.id}")

session.close()
