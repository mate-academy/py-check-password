import re


def check_password(password: str) -> bool:
    if not 8 <= len(password) <= 16:
        return False

    if not re.fullmatch(r"[A-Za-z0-9$@#&!\-_;]+", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[$@#&!\-_;]", password):
        return False

    return True
