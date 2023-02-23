def check_password(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False

    import re
    non_latin_chars = re.findall(r"[^a-zA-Z0-9$@#&!-_]", password)
    if non_latin_chars:
        return False

    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit, has_special])
