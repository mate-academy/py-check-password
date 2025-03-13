import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Їжакчочки", False),
        ("$0nG", False),
        ("$0ngBird_01234567", False),
        ("$ongBird", False),
        ("s0ngBird", False),
        ("$0ngbird", False)
    ],
    ids=[
        "test_if_latin",
        "test_length_at_least_8",
        "test_length_at_max_16",
        "test_at_least_1_digit",
        "test_at_least_1_special",
        "test_at_least_1_upper"
    ]
)
def test_if_latin(password: str, expected: bool) -> None:
    assert check_password(password) == expected
