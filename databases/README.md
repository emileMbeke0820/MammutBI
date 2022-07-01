# https://faker.readthedocs.io/en/master/providers/faker.providers.lorem.html
from datetime import datetime
from faker.factory import Factory
Faker = Factory.create
fake = Faker(locale="DE_de")
fake.seed(0)
ROWS=5
#-- generate Date
def generate_dates(_rows=ROWS, _format="%d/%m/%Y"):
     res = list()
     for _ in range(_rows):
          res.append(fake.date_object().strftime(_format))
     return res
#-- generate String
def generate_str(_rows=ROWS, _max_len=50):
     # text='Product Number: ????-########', letters='ABCDE'
     res = list()
     for _ in range(_rows):
          #res.append(fake.bothify(text="?"))
          res.append(fake.text(max_nb_chars=_max_len))
     return res
#-- generate Emails
def generate_email(_rows=ROWS):
     res = list()
     for _ in range(_rows):
          res.append(fake.free_email())
     return res
#-- generate German Phone : e.g. 0123/1234567
def generate_telefon(_rows=ROWS):
     res = list()
     for _ in range(_rows):
          #res.append(fake.msisdn()[:3] +"/"+ fake.msisdn()[:7])
          res.append(fake.msisdn())
     return res
#---------------
dates = generate_dates(ROWS, "%d.%m.%Y")
text = generate_str(ROWS)
email = generate_email(ROWS)
telefon = generate_telefon(ROWS)
for r in range(ROWS):
     print(dates[r], ";", text[r], ";", email[r], ";", telefon[r])