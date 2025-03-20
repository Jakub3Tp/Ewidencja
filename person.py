from datetime import date


class Address:
    def __init__(self, street, zipcode, city):
        self.street = street
        self.zipcode = zipcode
        self.city = city

class Person:
    def __init__(self, name, lastName, birthDate, pesel, street, zipcode, city):
        self.name = name
        self.lastName = lastName
        self.birthDate = birthDate
        self.pesel = pesel
        self.address = Address(street, zipcode, city)
        self.validate_pesel()

    def validate_pesel(self):
        if self.pesel.isdigit() and len(self.pesel) == 11:
            # 1-3-7-9-1-3-7-9-1-3.
            suma = ((int(self.pesel[0]) * 1) + (int(self.pesel[1]) * 3) + (int(self.pesel[2]) * 7)
                    + (int(self.pesel[3]) * 9) + (int(self.pesel[4]) * 1) + (int(self.pesel[5]) * 3)
                    + (int(self.pesel[6]) * 7) + (int(self.pesel[7]) * 9) + (int(self.pesel[8]) * 1)
                    + (int(self.pesel[9]) * 3))
            validate = (10 - (suma % 10) % 10)
            if validate == int(self.pesel[10]):
                year = int(self.pesel[0:2])
                month = int(self.pesel[2:4])
                day = int(self.pesel[4:6])

                if 81 <= month <= 92:
                    year += 1800
                    month -= 80
                elif 1 <= month <= 12:
                    year += 1900
                elif 21 <= month <= 32:
                    year += 2000
                    month -= 20
                elif 41 <= month <= 52:
                    year += 2100
                    month -= 40
                elif 61 <= month <= 72:
                    year += 2200
                    month -= 60

                birth_date = date(year, month, day)

                if birth_date == self.birthDate:
                    return True

        raise ValueError("Invalid pesel")