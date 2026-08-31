import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_basic_value_set(password: str, result: bool) -> None:
    assert check_password(password) is result


@pytest.mark.parametrize(
    "password,result",
    [
        ("Sh0rt!", False),
        ("VeryLong@ndV3ryStr0ngP@sswordTrustMe", False),
        ("M0der@tePass", True)
    ]
)
def test_password_length_boundaries(password: str, result: bool) -> None:
    assert check_password(password) is result


@pytest.mark.parametrize(
    "password,result",
    [
        ("M0deratePass", False),
        ("M0der@tePass", True)
    ]
)
def test_must_have_special_symbols(password: str, result: bool) -> None:
    assert check_password(password) is result


@pytest.mark.parametrize(
    "password,result",
    [
        ("m0der@tepass", False),
        ("M0der@tepass", True),
        ("m0der@tePass", True),
        ("M0der@tePass", True)
    ]
)
def test_must_have_uppercase_letter(password: str, result: bool) -> None:
    assert check_password(password) is result


@pytest.mark.parametrize(
    "password,result",
    [
        ("Moder@tePass", False),
        ("M0der@tePass", True)
    ]
)
def test_must_have_digit(password: str, result: bool) -> None:
    assert check_password(password) is result
