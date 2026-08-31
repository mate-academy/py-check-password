import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "checked_password,boolean",
    [
        ("Pass@word1", True),
        ("Alpha5bet!", True),
        ("Borjom7y&", True),
        ("aPos5tRo-f", True)
    ]
)
def test_for_true_passwords(checked_password: str, boolean: bool) -> None:
    assert check_password(checked_password) == boolean


@pytest.mark.parametrize(
    "checked_password,boolean",
    [
        ("Pasjhegrnkgheqenks@word1", False),
        ("Alphabet!", False),
        ("Qwertyu7", False),
        ("Ad$4", False),
        ("qwerty&7", False)






    ]
)
def test_for_false_passwords(checked_password: str, boolean: bool) -> None:
    assert check_password(checked_password) == boolean
