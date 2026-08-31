import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Pass@word1", True,
                     id="valid_password_1"),
        pytest.param("Str0ng@1", True,
                     id="valid_password_2"),
        pytest.param("A1@strongword", True,
                     id="valid_password_3"),
        pytest.param("qwerty", False,
                     id="invalid_too_short_1"),
        pytest.param("Short1@", False,
                     id="invalid_too_short_2"),
        pytest.param("ThisPasswordIsWayTooLong1@", False,
                     id="invalid_too_long"),
        pytest.param("NoDigits@", False,
                     id="invalid_no_digits"),
        pytest.param("nouppercase1@", False,
                     id="invalid_no_uppercase"),
        pytest.param("NOSPECIAL1", False,
                     id="invalid_no_special"),
        pytest.param("Invalid!Char^", False,
                     id="invalid_invalid_char"),
        pytest.param("Validpassword@", False,
                     id="invalid_no_digit"),
        pytest.param("Abcdefgh1@", True,
                     id="valid_boundary_case")
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
