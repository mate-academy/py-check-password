import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("P@ssw0rd123", True),
        ("paS$wordIncorrect123", False),
        ("pAssW0#", False),
        ("P@сsW0rд789", False),
        ("passWord1", False),
        ("p@ssword65", False),
        ("Q#4_erTy!", True)
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
