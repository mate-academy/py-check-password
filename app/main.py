def check_password(password: str) -> bool:
    if not (8 <= len(password) <= 16):
        return False

    special_allowed = set("$@#&-_")

    has_uppercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_allowed:
            has_special = True
        elif char.islower():
            pass
        else:
            return False

    return has_uppercase and has_digit and has_special
