from pytest import param, mark

from app.main import check_password


@mark.parametrize(
    "password,is_valid",
    [
        param("Любіть Україну❤️❤️", False,
              id="not latin password"),
        param("Abcde1@", False,
              id="small password"),
        param("AbcdeAbcdeAbcde1@", False,
              id="large password"),
        param("Abcdefgh@", False,
              id="no digit password"),
        param("Abcdefgh1", False,
              id="no special characters"),
        param("abcdefgh1@", False,
              id="no uppercase letter"),
        param("Abcdefgh1@", True,
              id="valid password"),
        param("Abcdef1@", True,
              id="min password"),
        param("AbcdeAbcdeAbcd1@", True,
              id="max password")
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
