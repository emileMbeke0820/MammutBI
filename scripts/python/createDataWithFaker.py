import csv
from faker import Faker

fake = Faker()


def createYourListe(profile):
    customer = []
    for i in range(0, profile):
        customer = [fake.random_number(digits=3), fake.name(), fake.address(),
                    str(fake.email()), str(fake.phone_number()),
                    fake.password(length=40, special_chars=False, upper_case=True),
                    fake.uuid4(), fake.iso8601()]

    with open('customer.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(customer)

    print("File has been created.")


if __name__ == '__main__':
    zahl = int(input("Enter the number of records:"))
    print(createYourListe(zahl))
