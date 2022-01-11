def input_postal_code(prompt, *postalcodes):
    while True:
        value = input(prompt)
        try:
            if value.lower() == 'q':
                return
            return _check_postal_code(value, postalcodes)
        except ValueError as Error:
            print(Error)


def _check_postal_code(value, postalcodes):
    try:
        p_code = int(value)
    except ValueError:
        raise ValueError(
            f"Please enter a valid postalcode, e.g., {postalcodes}.Your input '{value}' was not numerical.")

    if p_code not in postalcodes:
        raise ValueError(f"Please enter a valid postal code, "
                         f"your input {value} is not in the valid postal code list {postalcodes}")
    else:
        return value


def input_bounded_integer(prompt, description, minimum, maximum):
    while True:
        value = input(prompt)
        try:
            if value.lower() == 'q':
                return
            return _check_bounded_integer(value, description, minimum, maximum)
        except ValueError as Error:
            print(Error)


def _check_bounded_integer(value, description, minimum, maximum):
    try:
        b_int = int(value)
    except ValueError:
        raise ValueError(
            f"Please enter a valid {description}.Your input '{value}' was not numerical.")
    if not minimum <= b_int <= maximum:
        raise ValueError(
            f"Please enter a valid {description}, your input {value} is not between {minimum} and {maximum}.")
    else:
        return value
