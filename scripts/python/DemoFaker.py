import json
from faker import Faker

fake = Faker()


def createYourListe(profile):
    customer = {}
    for i in range(0, profile):
        customer[i] = {}
        customer[i]['id'] = fake.random_number(digits=3)
        customer[i]['name'] = fake.name()
        customer[i]['address'] = fake.address()
        customer[i]['email'] = str(fake.email())
        customer[i]['phone'] = str(fake.phone_number())
        customer[i]['traceId_tok'] = fake.password(length=40, special_chars=False, upper_case=True)
        customer[i]['customerId_tok'] = fake.uuid4()
        customer[i]['timestamp'] = fake.iso8601()

    with open('customer.json', 'w') as file:
        json.dump(customer, file)

    print("File has been created.")


if __name__ == '__main__':
    zahl = int(input("Enter the number of records:"))
    createYourListe(zahl)


