import pytest
from app.main import check_password


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("Pass@word1", True),
        ("Qwert@yy", False),
        ("Qwert@1", False),
        ("qwert@1yy", False),
        ("Qwert1yy", False),
        ("So1#@methingveryveryverylong", False)
    ]
)
def test_check_password(
        password: str,
        expected: bool,
) -> None:
    assert check_password(password) == expected
