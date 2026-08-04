import pytest
import app.main


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("Aa1!bbbb", True),
        ("Aa1!bbbbccccdddd", True),

        ("Aa1!bbb", False),
        ("Aa1!bbbbccccddddd", False),

        ("aa1!bbbb", False),
        ("Aaa!bbbb", False),
        ("Aa11bbbb", False),

        ("Aa1! bbbb", False),
        ("Aa1%bbbb", False),
        ("Пароль1!", False),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert app.main.check_password(password) == expected_result
