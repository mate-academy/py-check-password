from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        ("pass@word1", False),
        ("Pas@wo1", False),
        ("Pass@wo1", True),
        ("Pass@wooooooord1", True),
        ("Pass@woooooooord1", False),
        ("Password1", False),
        ("Pass^word1", False),
        ("Pass@wordi", False)
    ]
)
def test_should_not_return_true_with_incorrect_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
