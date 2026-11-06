def has_min_length(password):
    return len(password) >= 8
def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False
def has_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False
def has_lower(password):
    for char in password:
        if char.islower():
            return True
    return False
def has_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False
def validate_password(password):
    errors = []
    if not has_min_length(password):
        errors.append("Недостатня довжина")
    if not has_digit(password):
        errors.append("Немає цифри")
    if not has_upper(password):
        errors.append("Немає великої літери")
    if not has_lower(password):
        errors.append("Немає малої літери")
    if not has_special(password):
        errors.append("Немає спеціального символу")
    return len(errors) == 0, errors
def main():
    password = input("Введіть пароль: ")
    is_valid, errors = validate_password(password)
    if is_valid:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")

        for error in errors:
            print("Не виконано:", error)
main()
