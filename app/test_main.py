import pytest

from app.main import check_password


@pytest.mark.parametrize(
    ("password", "expected_result"),
    [
        pytest.param(
            "", False,
            id="should be at least 8 characters"
        ),
        pytest.param(
            "123456789@AaBbCcDd", False,
            id="should be maximum 16 characters inclusive"
        ),
        pytest.param(
            "@1aabbcc", False,
            id="should contains at least 1 uppercase letter"
        ),
        pytest.param(
            "@Aabbccd", False,
            id="should contains at least 1 digit"
        ),
        pytest.param(
            "1Aabbccd", False,
            id="should contains at least 1 special character"
        ),
        pytest.param(
            "$@#&!-_1Aa", True,
            id="special character should be from $@#&!-_"
        ),
        pytest.param(
            "фA!1234567", False,
            id="should accepts only letters of the Latin alphabet"
        ),
        pytest.param(
            "P@ssw0rd", True,
            id="'P@ssw0rd' should be True"
        ),
    ]
)
def test_function(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
