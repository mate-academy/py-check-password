from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "test_password, expected",
    [
        ("Mypa0#s", False),
        ("Mypasdasdasdasdasdasdasdasa", False),
        ("mypassword9#", False),
        ("Mypasswordв9#", False),
        ("Mypassword@#", False),
        ("Mypassword9", False),
        ("Successful_test1", True),
        ("Successful_test2", True),
        ("Successful_test3", True),
    ]
)
def test_check_password(test_password: str, expected: bool) -> None:
    assert check_password(test_password) == expected
