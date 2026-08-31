import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result", [
        ("A1@bcdef", True),
        ("Pass@word1", True),
        ("ABCdef1@", True),
        ("A1@bcdefghij", True),
        ("A1@bcdefghijklmn", True),
        ("P@word1", False),
        ("A1@bcdefghijklmnop", False),
        ("abcdefg1@", False),
        ("ABCDEFG@", False),
        ("ABCDEF12", False),
        ("1234567@", False),
        ("!!!!@@@@", False),
        ("A1@bcdef$", True),
        ("A1*bcdef", False),
        ("A1 bcdef", False),
        ("A1@bсdef", False),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
