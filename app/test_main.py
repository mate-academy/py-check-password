import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Q@1rty", False),
        ("kejvberkjv1@Wkjvbwkjvbwkj", False),
        ("kejvberkjv1@", False),
        ("kejvberkjvA@", False),
        ("kejvberkjv1AS", False)
    ]
)
def test_check_for_correct_password(password: str, result: bool) -> None:
    assert check_password(password) == result
