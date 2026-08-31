import pytest

from app.main import check_password


@pytest.mark.parametrize(
    ("password", "expected_result"),
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("fT34hgeemw", False),
        ("werqwet8#tr", False),
        ("Tuyjf#jfwen", False),
        ("Tiegj7iensw#nfwoeng", False),
        ("T4#f", False)
    ],
    ids=[
        "Should return True if password has all rules",
        "Should return False if password hasn't "
        "(upper letter, special char, digit) and not in range(8, 17)",
        "Should return False if password hasn't (digit) "
        "and not in range(8, 17)",
        "Should return False if password hasn't (special char)",
        "Should return False if password hasn't (upper letter)",
        "Shoudl return False if password hasn't (digit)",
        "Should return False if password not in range(8, 17)",
        "Should return False if password not in range(8, 17)",
    ]
)
def test_check_password(
    password: str,
    expected_result: str
) -> None:
    assert check_password(password) == expected_result
