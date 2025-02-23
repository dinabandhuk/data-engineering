import json
from faker import Faker

output = open("./scripts/data.JSON", "w")
fake = Faker()
alldata = {}
alldata['records'] = []

for x in range(10000):
    data={
        "name": fake.name(),
        "age": fake.random_int(min=18, max=100, step=1),
        "street": fake.street_address(),
        "city": fake.city(),
        "zip": fake.zipcode(),
        "lng": float(fake.longitude()),
        "lat": float(fake.latitude()),
    }
    alldata["records"].append(data)

json.dump(alldata, output)
output.close()