import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Pass@word", False),
        ("Pass@word1wertyuq", False),
        ("Password1w", False),
        ("P@word1", False),
        ("pass@word1", False),
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
