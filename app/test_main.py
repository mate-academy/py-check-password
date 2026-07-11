import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_basic_value_set_check(password: str, result: bool) -> None:
    assert check_password(password) is result
