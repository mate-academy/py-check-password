from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True,
                     id="should return True "
                        "if has_upper, has_digit, has_special"),
        pytest.param("qwe@1rty", False,
                     id="returns False for "
                        "passwords without uppercase letter"),
        pytest.param("Stoor1ing", False,
                     id="should  returns False "
                        "for passwords without special symbols"),
        pytest.param("", False,
                     id="should return False if no password"),
        pytest.param("Sopoitr@ng", False,
                     id=" returns False for passwords without digits"),
        pytest.param("Abcdwwefghijklmn1$A", False,
                     id="should return False if "
                        "password is longer than 16 characters"),
        pytest.param("k@E123", False,
                     id=" returns False for short passwords"),
        pytest.param("qW1werty%", False,
                     id="returns False if forbidden symbol appear"),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
