import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password_to_check,expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="everything correct"
        ),
        pytest.param(
            "Qwe@ty1",
            False,
            id="less then 8 characters"
        ),
        pytest.param(
            "Abbabagalamaga235$543",
            False,
            id="more then 16 characters"
        ),
        pytest.param(
            "Pass@wordhsfdgg",
            False,
            id="No digit in password"
        ),
        pytest.param(
            "Pass@word1hdпва",
            True,
            id="has non latin alphabet symbols"
        ),
        pytest.param(
            "pass@word1hsfdgg",
            False,
            id="No uppercase letter"
        ),
        pytest.param(
            "Password1hsfdgg",
            False,
            id="No special character"
        )
    ]
)
def test_check_correct_psw(
        password_to_check: str,
        expected_result: bool
) -> None:
    assert check_password(password_to_check) == expected_result
