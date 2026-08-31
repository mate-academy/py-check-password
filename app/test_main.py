import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("", False),
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word1Pass@word1", False),
        ("Stran@3!e", True),
        ("S1msd@", False),
        ("S@S!#$S123", True),
        ("ss@ss!231", False),
        ("ss@ss@Helloo", False),
    ]
)
def test_check_valid_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
