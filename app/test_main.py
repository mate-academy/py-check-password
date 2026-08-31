import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Le$$th7",
                     False,
                     id="Returns False if password is less than 7 chars"),
        pytest.param("1A2_17char_passY$",
                     False,
                     id="Returns False if password is larger than 16 chars"),
        pytest.param("no_upp3r_ca$e",
                     False,
                     id="Returns False if password has no any uppercase"),
        pytest.param("NoSpecials0",
                     False,
                     id="Returns False if password has no any special chars"),
        pytest.param("no_Digits",
                     False,
                     id="Returns False if password has no any digit chars")
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
