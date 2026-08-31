from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        ("dwedewdwed@wdd4", False),
        ("Q2@rtyuiopasdfghjk", False),
        ("#3Wd", False),
        ("sdfdg2WdQ", False),
        ("sdfdghWd#Q", False),
    ],

    ids=[
        "test_should_return_false_if_not_upper_letter",
        "test_should_return_false_if_more_than_max_length",
        "test_should_return_false_if_less_than_min_length",
        "test_should_return_false_if_not_special_symbols",
        "test_should_return_false_if_not_digit"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
