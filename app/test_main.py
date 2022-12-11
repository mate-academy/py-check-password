import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_good_password",
    [
        pytest.param("Pass@word1", True, id="correct password"),
        pytest.param("qwer@ty123", False, id="don't have upper letter"),
        pytest.param("Qwertyy@yyy", False, id="don't have a number"),
        pytest.param("Qwerty123", False, id="don't have special character"),
        pytest.param("@1Aa", False, id="lower than 8 characters"),
        pytest.param(
            "!1Aab!1Aab!1Aab!1Aab!1Aab",
            False,
            id="more than 16 characters"
        ),
        pytest.param("!ABCDEFGH@", False, id="don't have lower letter"),
        pytest.param("P@ssw0rd", True, id="length equal min 8 characters"),
        pytest.param(
            "P@ssw0rdP@ssw0rd",
            True,
            id="length equal max 16 characters")
    ]
)
def test_check_password(password: str, is_good_password: bool) -> None:
    assert check_password(password) == is_good_password
