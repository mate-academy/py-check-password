import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected_result", [
    pytest.param("Password123!", True, id="valid password"),
    pytest.param("Aa@1!", False, id="short password"),
    pytest.param("pass12@word", False, id="full lowercase password"),
    pytest.param("PASSWORD", False, id="full uppercase password"),
    pytest.param("Pass@word", False, id="digit absent password"),
    pytest.param("Password123", False, id="special chr absent password"),
    pytest.param("Paaaaaassssssswwwwoooo1@rd", False, id="long password")
])
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
