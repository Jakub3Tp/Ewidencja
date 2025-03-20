import sys

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog
from person import Person
from persons import Persons


class MyForm(QDialog):
    def __init__(self):
        self.ui = Ui_Dialog()
        super().__init__()
        self.persons = Persons()
        self.persons.load_from_file("dane.csv")
        self.ui.setupUi(self)
        self.ui.comboBox.addItems([f'{p.name} {p.lastName}' for p in self.persons.persons])
        self.ui.saveButton.clicked.connect(self.save_to_file)
        self.show()

    def save_to_file(self):
        name = self.ui.nameEdit.text()
        lastName = self.ui.lastNameEdit.text()
        birthDate = self.ui.dateEdit.date().toPyDate()
        pesel = self.ui.peselEdit.text()
        street = self.ui.streetEdit.text()
        zipCode = self.ui.zipCodeEdit.text()
        city = self.ui.cityEdit.text()

        try:
            self.persons.persons.append(Person(name, lastName, birthDate, pesel, street, zipCode, city))
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems([f'{p.name} {p.lastName}' for p in self.persons.persons])

        except ValueError as e:
            message = QMessageBox()
            message.setText(e.__str__())
            message.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyForm()
    app.exec()
    sys.exit(ex.persons.save_to_file("dane.csv"))

