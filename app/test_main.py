import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("ASdf1_", False),
        ("asdfjklHJLK_09789adfjklasd", False),
        ("asdfQWER1", False),
        ("ASdfjkld_", False),
        ("asdfhjkla", False),
        ("asdfhhjkl1_", False),
        ("HJKLHJKLHS_1", True),
        ("Qwert_1QWER", True)

    ]
)
def test_check_password_correct_output(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
