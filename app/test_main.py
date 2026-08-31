import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("ho3lH@e", False),
        ("derefgfdgdfgKdg@yy76876", False),
        ("123negJbr", False),
        ("ole@45671", False),
        ("hel@12G", False),
        ("kolWr@were", False),
    ]
)
def test_for_check_password_false(password: str,
                                  expected_result: bool) \
        -> None:
    assert check_password(password) == expected_result


@pytest.mark.parametrize(
    "password, expected_result",
    [

        ("hopl1@Nur", True),
        ("deewfH@1421", True),
        ("123negbr@H", True),
        ("ole45671@L", True),
        ("hell098@7A", True),
    ]
)
def test_for_check_password_true(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
