import validators

# print(validators.input_postal_code("Please enter your postal code (Enter 'q' to quit): ", 1010, 1020, 1030))
# print(validators.input_bounded_integer("Please enter age (Enter 'q' to quit): ", "age", 0, 130))
print(validators.input_bounded_integer("Please enter height in centimeters (Enter 'q' to quit): ", "height", 20, 250))
