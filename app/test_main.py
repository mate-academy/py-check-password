import pytest

from app.main import check_password


@pytest.mark.parametrize("password,result", ([
    pytest.param("password1234!", False,
                 id="password_must_contains_upper_letter"),
    pytest.param("PASSo@1", False,
                 id="length_must_be_equal_bigger_8"),
    pytest.param("PASSWWWwwwwwooorrrd123!@#$", False,
                 id="length_must_be_less_equal_16"),
    pytest.param("FSAFFAS132!", True,
                 id="corrected_password"),
    pytest.param("VPXCVPPNBI412", False,
                 id="password_must_contains_special_character"),
    pytest.param("WWR@$Dvsdsg", False,
                 id="password_must_contains_digits")]))
def test_password(password: str, result: bool) -> None:
    assert check_password(password) is result
