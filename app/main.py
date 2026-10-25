def check_password(password: str) -> bool:
    if not 8 <= len(password) <= 16:
        return False

    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if "A" <= char <= "Z":
            has_upper = True
        elif "a" <= char <= "z":
            continue
        elif "0" <= char <= "9":
            has_digit = True
        elif char in "$@#&!-_":
            has_special = True
        else:
            return False

    return has_upper and has_digit and has_special
