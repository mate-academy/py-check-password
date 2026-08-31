import pytest as pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password  ,expect_result",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Password1", False),
        ("Passw@1", False),
        (
            "Passwwwwwwwwwwww@@@1",
            False,
        ),
    ],
)
def test_should_return_expected_check_passwords(
    password: str,
    expect_result: str
) -> None:
    password = password
    assert check_password(password) == expect_result
