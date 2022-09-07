from django.core.management.base import BaseCommand
from demo.models import Person
from faker import Faker
import random

fake = Faker()

ROLE_CHOICES = ["M", "O", "A"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        Person.objects.all().delete()
        for _ in range(100):
            Person.objects.create(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                title=fake.job(),
                email=fake.email(),
                role=random.choice(ROLE_CHOICES),
                likes_dogs=fake.boolean(),
                likes_cats=fake.boolean(),
                dob=fake.past_date(start_date="-100y"),
                bio=fake.paragraph(),
                phone=fake.random_number(digits=10),
            )
