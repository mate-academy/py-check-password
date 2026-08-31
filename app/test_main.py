import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "user_password, expected_check",
    [
        ("Pass@word1", True),
        ("$qwerty11", False),
        ("$Str@nggg", False),
        ("_123456789", False),
        ("П#ар9ол1215", False),
        ("Pass@1", False),
        ("Pass@1word@2Pass@3word@4Pass@5word@6Pass@7word", False),
        ("PASS@WORD1", True),
    ],
    ids=[
        "len norm and are all rules - return True",
        "len norm and without Upper - return False",
        "len norm and without number - return False",
        "len norm and without letter - return False",
        "len norm and without ascii - return False",
        "len short and are all rules - return False",
        "len long and are all rules - return False",
        "len norm and without lower - return True",
    ]
)
def test_check_password(
        user_password: str,
        expected_check: bool) -> None:
    assert check_password(user_password) == expected_check
