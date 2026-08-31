from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Pa@wor1", False),
        ("Pass@word123456789", False),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass@word", False),
    ],
    ids=[
        "check_correct_password",
        "check_min_lengh",
        "check_max_lengh",
        "check_only_lowercase",
        "check_without_spec_char",
        "check_without_num"
    ]
)
def test_check_correct_password(password: str, result: bool) -> None:
    assert check_password(password) is result
