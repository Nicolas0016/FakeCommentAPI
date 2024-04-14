from faker import Faker
from random import randint



def generate_DNI():
    id = str(randint(0, 99999999))
    while len(id) != 8:
        id = "0" + id
    return id


def generate_name(fake):
    data = fake.name().split(" ")
    if len(data) == 2:
        [name, last_name] = data
    elif len(data) == 3: 
        name = data[:1]
        last_name = data[2]
    elif len(data) == 4:
        name = data[:1]
        last_name = data[2:3]
    return {'name': name, 'last_name': last_name}


def generate_age():
    return randint(19, 77)


def generate_country(fake):
    return fake.country()

def comment(fake):
    return fake.text()

def fake_api(render, country):
    fake = Faker([country])
    request = []
    for i in range(render):
        name = generate_name(fake)
        data = { 
            "id": i,
            "DNI": generate_DNI(),
            "name": name["name"],
            "lastName": name["last_name"], 
            "age": generate_age(), 
            'country': generate_country(fake),
            'comment': comment(fake)}
        request.append(data)
    return request



