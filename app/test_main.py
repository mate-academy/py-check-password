import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "checked_password,expected_result",
    [
        ("Pass@word1", True),
        ("Пass@word1", False),
        ("Pass@word1)", False),
        ("Ps@wrd1", False),
        ("Pass@word1Pass@word1", False),
        ("Pass@word", False),
        ("pass@word1", False),
        ("Password1", False)
    ]
)
def test_should_return_correct_bool(
        checked_password: str,
        expected_result: bool
) -> None:
    assert check_password(checked_password) == expected_result
