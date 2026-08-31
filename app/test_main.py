import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="test when ony accepted characters included"
        ),
        pytest.param(
            "Pass@word1*-*",
            False,
            id="test when unaccepted characters included"
        ),
        pytest.param(
            "Pass@t1",
            False,
            id="test when password length is 7 characters"
        ),
        pytest.param(
            "Pass@word11111111",
            False,
            id="test when password length is 17 characters"
        ),
        pytest.param(
            "1111111134$2",
            False,
            id="test when letters missing in password"
        ),
        pytest.param(
            "Dhdhwiwwo$",
            False,
            id="test when numbers missing in password"
        ),
        pytest.param(
            "Password1",
            False,
            id="test when special characters missing in password"
        ),
        pytest.param(
            "password1",
            False,
            id="test when uppercase missing in password"
        ),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
