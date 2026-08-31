import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("@Lqw2y", False),
        ("Hijflk_lsihdflkjhsdflk2kji", False),
        ("lkhdljhk1_", False),
        ("Lkjhsdjnj@", False),
        ("djLjhbsd1", False),
        ("Pass@word1", True)
    ],
    ids=[
        "should return False if password length"
        " is less then 8 characters",
        "should return False if password length "
        "is more then 16 characters",
        "should return False if password "
        "doesn't contain an uppercase letter",
        "should return False if password "
        "doesn't contain a digit",
        "should return False if password "
        "doesn't contain a special character",
        "should return True if password is valid",
    ]
)
def test_return_value_with_different_passwords(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
