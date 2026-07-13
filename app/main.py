def check_password(password: str) -> bool:
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$@#&!-_"
    for char in password:
        if char not in allowed_chars:
            return False
    return True
