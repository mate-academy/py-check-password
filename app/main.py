from string import ascii_letters, digits


def check_password(password: str) -> bool:
    if not 8 <= len(password) <= 16:
        return False

    has_uppercase = any(letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letter in password)
    has_digit = any(letter in digits for letter in password)
    has_special = any(letter in "$@#&!-_" for letter in password)
    allowed_characters = ascii_letters + digits + "$@#&!-_"

    return (
        all(letter in allowed_characters for letter in password)
        and has_uppercase
        and has_digit
        and has_special
    )
