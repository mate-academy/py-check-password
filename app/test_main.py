import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "string,res",
    [
        ("He11@", False),
        ("He11o@LongPassword", False),
        ("He11o@LongPaass1", True),
        ("HelloPass@", False),
        ("He11oPass", False),
        ("hello@pass1", False),
        ("Hell0@Str", True)
    ],
    ids=[
        "Too short pass",
        "Too long pass",
        "Longest allowable pass",
        "Pass without numbers",
        "Pass without special characters",
        "Pass without capital letters",
        "Good pass"
    ]
)
def test_check_password(string: str, res: bool) -> None:
    assert check_password(string) == res
