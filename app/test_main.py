import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("s8#Qdh9", False),
        ("R$biK0n1", True),
        ("Huho0polski@0-ft", True),
        ("Huho0polski@0-ft1", False)
    ],
    ids=[
        "password has 7 characters",
        "password has 8 characters",
        "password has 16 characters",
        "password has 17 characters"
    ]
)
def test_password_has_8_16_characters_inclusive(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password,result",
    [
        ("R$bOoiK0n1#&!_-", True),
        ("%'/|*+=&^'ПР/п'ц?у", False),
    ],
    ids=[
        "password consist of only allowed characters",
        "password has unsupported characters",
    ]
)
def test_password_consist_of_only_allowed_characters(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password,result",
    [
        ("R$iiKEnR", False),
        ("R$iiK0n1", True),
        ("Huo0polski00Fft1", False),
        ("Huo0lski@0Fft1", True),
        ("huho0lski@0-t1", False),
        ("Huho0lSki@0-ft", True)
    ],
    ids=[
        "password has no digit",
        "password has at least 1 digit",
        "password has no special character",
        "password has at least 1 special character",
        "password has no uppercase",
        "password has at least 1 uppercase"
    ]
)
def test_password_has_at_least_1_digit_1_special_1_uppercase(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
