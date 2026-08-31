import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "string, expected",
    [
        pytest.param(
            "aAb12kj~",
            False,
            id="test password contains prohibited symbol"
        ),
        pytest.param(
            "a1@J",
            False,
            id="test length less than 8"
        ),
        pytest.param(
            "12aABC!@",
            True,
            id="test password length are 8"
        ),
        pytest.param(
            "123456789abcABC!@ABC",
            False,
            id="test length more than 16"
        ),
        pytest.param(
            "123456789aABC!@A",
            True,
            id="test password length are 16"
        ),
        pytest.param(
            "12aabc!@",
            False,
            id="test password does not contains uppercase letter"
        ),
        pytest.param(
            "12aabcAD",
            False,
            id="test password does not contains special symbol"
        ),
        pytest.param(
            "!@aabcAD",
            False,
            id="test password does not contains numbers"
        )
    ]
)
def test_check_password(string: str, expected: bool) -> bool:
    assert check_password(string) == expected
