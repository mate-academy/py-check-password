import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("1A$@#&!-_", True, id="Special symbols"),
        pytest.param("1234567890A_", True, id="Digits 0-9"),
        pytest.param("Abcde@7", False, id="Too short"),
        pytest.param("123456789012345@A", False, id="Too long"),
        pytest.param(
            "Password1", False, id="Does not contain special symbols"
        ),
        pytest.param(
            "qwerty1#", False, id="Does not contain uppercase letter"
        ),
        pytest.param("P@ssword", False, id="Does not contain digits")
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
