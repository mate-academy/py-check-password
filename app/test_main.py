import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param(
            "",
            False,
            id="False when password is empty string"),
        pytest.param(
            "Acde12$",
            False,
            id="False when password less than minimum length"),
        pytest.param(
            "Asdfghqwer123456!@",
            False,
            id="string longer than max length"),
        pytest.param(
            "qwertyuiopA!",
            False,
            id="password does not contain any digit"),
        pytest.param(
            "qwertyjj34!",
            False,
            id="pasword should contain letter in uppercase"),
        pytest.param(
            "Adghjl1234",
            False,
            id="No any special symbol in password"),
        pytest.param(
            "Azxcv123@",
            True,
            id="valid password")
    ]
)
def test_check_password(
    password: str,
    expected_result: str
) -> None:
    assert check_password(password) == expected_result
