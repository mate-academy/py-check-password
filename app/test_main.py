import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Riabo$4",
                     False,
                     id="Return False if password is less than 7 chars"),
        pytest.param("1Qertyuiopa$34567",
                     False,
                     id="Return False if password is larger than 17 chars"),
        pytest.param("w1thout_upper$",
                     False,
                     id="Return False if password without upper case"),
        pytest.param("WithoutSp3c",
                     False,
                     id="Return False if password without specials"),
        pytest.param("Without_digits",
                     False,
                     id="Return False if password without digits")
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
