import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("pass#word1", False),
        ("Pass#wordT", False),
        ("B4g$b", False),
        ("Bugs@bunny4Lola@Bunny5", False),
        ("Bugsbunny1", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
