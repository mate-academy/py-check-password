import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "initial_password,"
    "expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("PabloNeruda!5", True),
        ("PabloNeruda!", False),
        ("PabloNeruda!5_was_vegetarian", False),
        ("pabloneruda!5", False),
        ("aaf", False),
        ("wreterN8", False),
        ("P@ne35", False)
    ],
)
def test_checking_is_correct(
        initial_password: str,
        expected_result: bool
) -> None:
    assert check_password(initial_password) == expected_result
