import random
import string
from faker import Faker

fake = Faker()

class RandomData:

    def randomFirstName(self):
        return fake.first_name()

    def randomLastName(self):
        return fake.last_name()

    def randomEmailId(self):
        return fake.email()

    def randomtelephone(self):
        return fake.phone_number()

fakedata = RandomData()