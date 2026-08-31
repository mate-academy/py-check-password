from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result", [
        ("Pass@word1", True),
        ("Qwertyyy#", False),
        ("1wertyyy#", False),
        ("s1r@ng", False),
        ("F_1dffgghhjjkkklllllllllllll#", False),
        ("Password123", False),
        ("5A@", False),

    ],
    ids=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result, f"{password} is {result}"
