from faker import Faker
import csv
output = open('./scripts/data.csv', 'w')
fake = Faker()
header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']
mywriter = csv.writer(output)
mywriter.writerow(header)

for r in range(10000):
    mywriter.writerow([
        fake.name(), 
        fake.random_int(
            min=18,
            max=100,
            step=1
        ),
        fake.street_address(),
        fake.city(),
        fake.state(),
        fake.zipcode(),
        fake.longitude(),
        fake.latitude(),
    ])

output.close()