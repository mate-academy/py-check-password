import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("UPPERCASEONLY", False),
        ("Noodigit@", False),
        ("NoSpecial5", False),
        ("noupper5$", False),
        ("aCD#4", False),
        ("Abcdefghjka#skdj1", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
