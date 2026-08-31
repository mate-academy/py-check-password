import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("Qw&rty5", False),
        ("Qw&rtyuiopasdfgh7", False),
        ("p@ssword1", False),
        ("P@ssword", False),
        ("Password1", False),
    ]
)
def test_password_checker(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
