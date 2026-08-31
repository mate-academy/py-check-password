import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "input_password,result", [
        pytest.param("Pass@word1", True, id="Valid password"),
        pytest.param("qwert1y@", False,
                     id="Valid password length but without uppercase letter"),
        pytest.param("Str@ngqw", False,
                     id="Valid password length but without digit"),
        pytest.param("Str1qwer", False,
                     id="Valid password length but without special character"),
        pytest.param("Str1ng@", False,
                     id="Valid characters but "
                        "password length less then needed"),
        pytest.param("Pass@word1Pass@wo", False,
                     id="Valid characters but "
                        "password length more then needed")
    ])
def test_check_password(input_password: str, result: bool) -> None:
    assert check_password(input_password) == result
