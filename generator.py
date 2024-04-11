import random

from data import User
from faker import Faker

faker_en = Faker("En")
Faker.seed()
def generated_user(phone_len):
    yield User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        full_name=generated_name(),
        phone_number=generated_phone_number(phone_len)
    )

def generated_name():
    female = faker_en.name_female()
    male = faker_en.name_male()
    return random.choice([male, female])

def generated_phone_number(n):
    phone_len = n - 4
    number = "+995" + "".join([str(random.randint(0, 9)) for _ in range(phone_len)])
    return number

a = next(generated_user(30))
print(a.first_name)
print(a.last_name)
print(a.full_name)
print(a.phone_number)
print(generated_phone_number(7))