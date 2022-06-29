"""
Checkout Faker and create Fake Data for future use.
"""
import json

from faker import Faker

fake = Faker()

def createYourListe():
    kunde = []
    for i in range(1, 11):
        i = fake.profile()
        kunde.append(i)

    print(kunde)


if __name__ == '__main__':
    createYourListe()


