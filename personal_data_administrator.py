from validators import input_string, input_bounded_integer, input_postal_code
import csv


# print(validators.input_postal_code("Please enter your postal code (Enter 'q' to quit): ", 1010, 1020, 1030))
# print(validators.input_bounded_integer("Please enter age (Enter 'q' to quit): ", "age", 0, 130))
# print(validators.input_bounded_integer("Please enter height in centimeters (Enter 'q' to quit): ", "height", 20, 250))
list_of_persons = []
person = {}

list_of_persons.append(person)

prompt = "Please choose which aspect to edit: (n)ame, (p)ostal code, (a)ddress, (c)ity, (d)ay of birth, " \
         "(m)onth of birth, (y)ear of birth (or enter 'q' to quit): "

while True:
    aspect = input(prompt)

    match aspect.casefold()[:1]:
        case 'n':
            person.update({"name": input_string("Please enter name (Enter ‚q‘ to quit): ")})
        case 'p':
            person.update({"postal code": input_postal_code("Please enter your postal code (Enter 'q' to quit): ", 1010,
                                                            1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100)})
        case 'a':
            person.update({"address": input_string("Please enter your address (Enter ‚q‘ to quit): ")})
        case 'c':
            person.update({"city": input_string("Please enter your city (Enter ‚q‘ to quit): ")})
        case 'd':
            person.update({"day of birth": input_bounded_integer("Please enter day of birth (Enter 'q' to quit): ",
                                                                 "day of birth", 1, 31)})
        case 'm':
            person.update({"month of birth": input_bounded_integer("Please enter month of birth (Enter 'q' to quit): ",
                                                                   "month of birth", 1, 12)})
        case 'y':
            person.update({"year of birth": input_bounded_integer("Please enter year of birth (Enter 'q' to quit): ",
                                                                  "year of birth", 1930, 2021)})
        case 'q':
            break


with open('people.csv', 'w', newline='', encoding="UTF-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(person.keys())
    writer.writerow(person.values())
