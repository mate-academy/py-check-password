import pytest
from .main import check_password


@pytest.mark.parametrize(
    "password, expected_result", [
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("Pass@word1234567890", False),
        ("Pass@1", False),
        ("Pass@word1", True),
    ]
)
def test_should_return_expected_result(password: str,
                                       expected_result: bool) -> None:

    assert check_password(password) == expected_result
