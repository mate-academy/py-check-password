import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("алорофлл848В!", False),
        ("3jffjDd!", True),
        ("1!fDfjd", False),
        ("hdjfdiKjfgb@543j", True),
        ("kjzhdfkj8^", False),
        ("fjfkdjsfk", False),
        ("12234234", False),
        ("@@@@@@@@@@", False),
        ("Dkjkjndkank6476!fdfdf", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
