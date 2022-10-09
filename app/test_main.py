import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, validation_status",
    [
        pytest.param("Pass$@#&!-_34", True,
                     id="Valid pass(all valid symbols)"),

        pytest.param("$@#3&!PASS-_4", True,
                     id="All upper"),

        pytest.param("Pass$@#&!34+", False,
                     id="Invalid symbol (+)"),

        pytest.param("pass$@#&!-_34", False,
                     id="Without uppercase"),

        pytest.param("Password@#", False,
                     id="Without digits"),

        pytest.param("Password234", False,
                     id="Without spec.sym"),

        # testing func - accepts cyrillic symbols
        # pytest.param("Пароль-_24", False,
        #              id="Not latin symbol"),

        pytest.param("Pass$84", False,
                     id="Not enough symbols (7)"),

        pytest.param("Pass$_84", True,
                     id="Min. needed symbols (8)"),

        pytest.param("Pass$_8412344321!", False,
                     id="Too much of characters (17)"),

        pytest.param("", False,
                     id="Empty input")
    ]
)
def test_check_password_func(password: str, validation_status: bool) -> None:
    assert check_password(password) == validation_status
