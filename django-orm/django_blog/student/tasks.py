from django.db import transaction
from faker import Faker
from .models import Student
import random

fake = Faker()

def add_students(num_students=20):

    """Add fake students to the list of students"""

    with transaction.atomic():
        for _ in range(num_students):
            firstname = fake.first_name()
            surname = fake.last_name()
            age = random.randint(18, 30)
            classroom = random.randint(1, 12)
            teacher = fake.name()
            Student.objects.create(firstname=firstname, surname=surname, age=age, classroom=classroom, teacher=teacher)