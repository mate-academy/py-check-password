import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty-1", False),
        ("Qwe-ty1", False),
        ("Qwer-tyy", False),
        ("Qwerrty1", False),
        ("@Qwerty1@Qwerty1", True),
        ("@Qwerty1@Qwerty12", False),
    ],
    ids=[
        "ideal password",
        "should have upper letter",
        "should have minimum 8 symbols",
        "should have minimum 1 number",
        "should have minimum 1 spec symbols",
        "limit value check",
        "excess limit symbols"
    ],
)
def test_check_password(
    password: str,
    expected_result: bool
) -> None:
    assert check_password(password) == expected_result
