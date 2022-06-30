import csv
import json
from faker import Faker

fake = Faker()



def createYourListe(profile):
    customer = []
    for i in range(0, profile):
        kunde = {}
        kunde['id'] = fake.random_number(digits=3)
        kunde['name'] = fake.name()
        kunde['address'] = fake.address()
        kunde['email'] = str(fake.email())
        kunde['phone'] = str(fake.phone_number())
        kunde['traceId_tok'] = fake.password(length=40, special_chars=False, upper_case=True)
        kunde['customerId_tok'] = fake.uuid4()
        kunde['timestamp'] = fake.iso8601()
        customer.append(kunde)

    with open('customer.json', 'w') as file:
        file.write("[")
        attachment = ",\n"
        for a,d in enumerate(customer):
            if(a == len(customer)-1):
                attachment = "\n"
            file.write(json.dumps(d) + attachment)
        file.write("]")








    print("File has been created.")


if __name__ == '__main__':
    createYourListe(4)


