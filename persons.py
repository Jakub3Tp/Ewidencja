from operator import index

from person import Person
from datetime import date


class Persons:

    def __init__(self):
        self.persons = []

    def save_to_file(self, path):
        with open(path, 'w') as file:
            for person in self.persons:
                file.write(f"{person.name};{person.lastName};{person.birthDate};{person.pesel};"
                           f"{person.address.city};{person.address.street};"
                           f"{person.address.zipcode}\n")


    def load_from_file(self, path):
        with open(path, 'r') as file:
            data = file.read()

        if data != "":
            data = data.split("\n")
            for person in data:
                if person != "":
                    person_data = person.split(";")
                    name = person_data[0]
                    last_name = person_data[1]
                    birth_date = date.fromisoformat(person_data[2])
                    pesel = person_data[3]
                    city = person_data[4]
                    street = person_data[5]
                    zipcode = person_data[6]

                    self.persons.append(Person(name, last_name, birth_date, pesel, street, zipcode, city))

