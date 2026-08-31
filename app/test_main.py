import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("qwesdfsRt2y", False),
        ("Str@ngtrf", False),
        ("", False),
        ("Tsfs2@", False),
        ("DanyaTrukh@nov1sCoolGuy", False),
        ("helloworl$d1", False)
    ],
    ids=[
        "returns True if password is good",
        "returns False if password without special symbols",
        "returns False if password without digits",
        "returns False if password is empty",
        "returns False if password too short",
        "returns False if password too long",
        "returns False if password without uppercase letter"
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
