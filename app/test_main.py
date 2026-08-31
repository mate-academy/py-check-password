import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("Gk5!$@#&!-_", True,
                     id="check if valid with all conditions are met"),
        pytest.param("Gk5!$@#/!-_", False,
                     id="check if not valid with not allowed symbols"),
        pytest.param("Gk5!", False,
                     id="check if not valid with too short length"),
        pytest.param("Gk5!$@#!-kkkkkkkkkk_", False,
                     id="check if not valid with too long length"),
        pytest.param("Gk!$@#cvcxc!-_", False,
                     id="check if not valid with no digit"),
        pytest.param("Gk5dsdasdas", False,
                     id="check if not valid with no special character"),
        pytest.param("ak5!$@#!-_", False,
                     id="check if not valid with no capital letter"),

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
