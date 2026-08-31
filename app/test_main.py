import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "input_data, result",
    [
        ("Hel@o_#8", True),
        ("Hel@_#8", False),
        ("Hel@o_#018", True),
        ("Hel@o_#8He@lo_#8", True),
        ("Hel@o_#8Hel@o_#83", False),
        ("Without_digits", False),
        ("MMMmmm___000", True),
        ("small_letters12", False),
        ("12345__987$", False),
        ("Hel@o_#08?", False),
        ("OIUKJHK_89", True),
        ("////????12", False),
    ],
    ids=[
        "contain at least 8 characters 'T'",
        "contain less then 8 characters 'F'",
        "contain within 8-16 characters 'T'",
        "contain less then 16 characters 'T'",
        "contain more then 16 characters 'F'",
        "without digits, 'F'",
        "contain allowed symbols repeated, 'T'",
        "without uppercase letter, 'F'",
        "without letters, 'F'",
        "contain not particular symbols 'F'",
        "contain uppercase letters only 'T'",
        "contain not allowed symbols, 'F'"
    ]
)
def test_check_password(input_data: str, result: bool) -> None:
    assert check_password(input_data) == result
