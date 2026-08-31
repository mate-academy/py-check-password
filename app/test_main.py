import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("Password1", False),
        ("Pa$8", False),
        ("Pass@word", False),
        ("TheSrongerPass@word1", False)
    ],
    ids=[
        "Should return True if password is valid",
        "Should returns False for passwords without uppercase letter",
        "Should returns False for passwords without special symbols",
        "Should returns False for short passwords",
        "Should returns False for passwords without digits",
        "Should returns False for too long passwords"
    ]
)
def test_should_return_correct_result(password: str,
                                      expected_result: bool) -> None:
    assert check_password(password) == expected_result
