import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "string, expected",
    [
        ("Pass@word1", True),
        ("qwer@Rty", False),
        ("Str@ng", False),
        ("", False),
        ("letterasda1@s", False),
        ("Aaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaa@", False),
        ("Aa@1", False),
        ("aFawd1qasq", False),
    ]
)
def test(string: str, expected: bool) -> None:
    assert (
        check_password(string) == expected
    )
