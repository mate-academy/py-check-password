import pytest

from .main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("сCccc@ccc", False),
        ("noupperc@s3", False),
        ("VerYL0nGP@ssworD123456", False),
        ("Nospecsymbo1", False),
        ("P@55", False)

    ], ids=[
        "Proper password",
        "weak password",
        "no numbers",
        "Non latin letters",
        "no upper case",
        "too many symbols",
        "no special symbols",
        "too short password"
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
