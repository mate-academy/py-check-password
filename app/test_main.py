import pytest
from unittest.mock import Mock
from app.main import check_password


@pytest.mark.parametrize(
    "password,value",
    [
        ("Pa@word1", True),
        ("P@woet1", False),
        ("Pass@wordd", False),
        ("pass@word1", False),
        ("Pacvbss23dcv2344@", False)
    ]
)
def test_check_password(password: Mock, value: Mock) -> None:
    assert check_password(password) == value
