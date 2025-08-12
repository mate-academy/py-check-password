from app.main import check_password

# ✅ Валідні паролі
def test_valid_password_min_length():
    assert check_password("A1@bcdef") == True  # рівно 8 символів

def test_valid_password_max_length():
    assert check_password("Abcdefghij1@KLMN") == True  # рівно 16 символів

def test_valid_password_with_all_requirements():
    assert check_password("Pass@word1") == True

# ❌ Невалідні паролі — довжина
def test_too_short_password():
    assert check_password("A1@bcde") == False  # 7 символів

def test_too_long_password():
    assert check_password("Abcdefghij1@KLMNO") == False  # 17 символів

# ❌ Невалідні паролі — відсутні компоненти
def test_missing_uppercase():
    assert check_password("password1@") == False  # немає великої літери

def test_missing_digit():
    assert check_password("Password@") == False  # немає цифри

def test_missing_special_symbol():
    assert check_password("Password1") == False  # немає спецсимвола

# ❌ Невалідні паролі — недозволені символи
def test_invalid_character():
    assert check_password("Password1%") == False  # '!' не входить у список дозволених

def test_invalid_unicode():
    assert check_password("Пароль1@") == False  # кирилиця

def test_invalid_space():
    assert check_password("Pass word1@") == False  # пробіл

# ❌ Невалідні паролі — порожній рядок
def test_empty_password():
    assert check_password("") == False
