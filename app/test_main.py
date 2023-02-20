import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_string,output_bool", [
        ("Az8dartv", False),
        ("Az8dart#", True),
        ("Az8dar#", False),
        ("@#!-__A#", False),
        ("123456#8", False),
        ("Az8dart#36FasX-1", True),
        ("Az8dart#36FasX-12", False),
    ],
    ids=[
        "No special provided",
        "Everything provided, min range",
        "Everything provided, exceed min range",
        "Only specials and uppercase",
        "Only digits and specials",
        "Everything provided, max range",
        "Everything provided, exceed max range",
    ]
)
def test_check_password_output(input_string: str,
                               output_bool: str) -> None:
    assert check_password(input_string) == output_bool
