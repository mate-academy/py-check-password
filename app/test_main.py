import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("da4@Z", False),
        ("daD@Zdad90dzwqDWAZ66f", False)
    ]
)
def test_return_false_if_len_invalid(password: str, result: bool) -> None:
    assert check_password(password) == result, (
        "Length should be in range from 8 to 16 inclusive"
    )


@pytest.mark.parametrize(
    "password,result",
    [
        ("da4ASDr53Z", False),
        ("ZXCZe342GGR", False),
        ("ZXCZe!42GGR", True)
    ]
)
def test_should_have_special_character(password: str, result: bool) -> None:
    assert check_password(password) == result, (
        "Password should have a special character"
    )


@pytest.mark.parametrize(
    "password,result",
    [
        ("fasFEW!@TSFZ", False),
        ("CZXTfcddsV!@", False)
    ]
)
def test_should_have_digit(password: str, result: bool) -> None:
    assert check_password(password) == result, (
        "Password should have a digit"
    )


@pytest.mark.parametrize(
    "password,result",
    [
        ("da4@xdadwa", False),
        ("dwadhr2245s!txf", False)
    ]
)
def test_should_have_uppercase_letter(password: str, result: bool) -> None:
    assert check_password(password) == result, (
        "Password should have an uppercase letter"
    )


@pytest.mark.parametrize(
    "password,result",
    [
        ("фвыФВ56!@6", False),
        ("2DAіФВ16!$", False),
        ("adgFFC2AX16!$", True)
    ]
)
def test_should_accept_only_latin_alphabet(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result, (
        "Function should accept only latin alphabet in password"
    )
