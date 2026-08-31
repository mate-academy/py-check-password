import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Password1", False),
        ("qwert1wdz@", False),
        ("strongerr", False),
        ("S1ow@", False),
        ("Ghj2@lkfjhdasdffffq", False),
        ("Qwert#wer", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
