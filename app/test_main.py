import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, answer",
    [
        ("Password1", False),
        ("qwerty", False),
        ("1Qwertyui", False),
        ("1Qwer@tyui", True),
        ("1Qwertyui$9023g", True),
        ("1wertyui$9023g", False),
        ("1Qwertyui$9023gwq1", False),
        ("Qwer@tyui$g", False),
        ("1Qwe$", False),
        ("1Qwertyui923g", False)
    ]
)
def test_check_password(password: str, answer: bool) -> None:
    assert check_password(password) == answer
