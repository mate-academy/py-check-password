import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "initial_password, expected_result",
    [
        ("Pass@word1", True),
        ("qP&1", False),
        ("Str@ng", False),
        ("gjgfl12$Pf&4", True),
        ("piddubN89", False),
        ("232jktyfhPn&bfkPPPdd", False),
        ("piddubn9&", False),
        ("Pid&nmfj", False)
    ],
    ids=[
        "Good job!",
        "too short password, at least 8 letters",
        "should be at least 8 letters",
        "Correct!",
        "no special sign",
        "too long password, maximum 16 letters",
        "no uppercase letter",
        "no digits!"
    ]
)
def test_check_password(initial_password: str, expected_result: bool) -> None:
    assert check_password(initial_password) == expected_result
