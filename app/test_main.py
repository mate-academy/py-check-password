import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@wo1", True),
        ("Pass@wo1Pass@wo1", True),
        ("Pass@word1Pass@word1", False),
        ("Pa@1", False),
        ("Pass@word", False),
        ("Pass@word", False),
        ("Password1", False),
        ("@assword1", False),
        ("@asswoвd1", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
