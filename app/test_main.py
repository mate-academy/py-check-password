import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Aa_0-9@", False, id="<8 symbols"),
        pytest.param("Aa_0-9@#", True, id="valid min symbols"),
        pytest.param("Aa_0-9@!!!!!!!!!!", False, id=">16 symbols"),
        pytest.param("Aa_0-9@!!!!!!!!!", True, id="valid max symbols"),
        pytest.param("aaaaaaaa", False, id="only lower"),
        pytest.param("aaaaaaaa1", False, id="lower, digit"),
        pytest.param("aaaaaaaa1#", False, id="lower, digit, sc"),
        pytest.param("aaaaaaaa1#A", True, id="valid"),
        pytest.param("$$@#&!-_", False, id="only special char"),
        pytest.param("", False, id="empty"),
        pytest.param("        ", False, id="only spaces"),
        pytest.param("aaaa aaa1#A", False, id="contains spaces"),
        pytest.param("aaaaaa1#Añ", False, id="contains non-Latin char"),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result
