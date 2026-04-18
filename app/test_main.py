import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("Str@ng", False),
        ("@W1erty", False),
        ("A#2njdijanjdijcaj", False),
        ("432345676", False),
        ("$@#&!-_$@#&!-_", False),
        ("ahfunjvos", False),
        ("a1@asdfghj", False),
        ("AB@asdfghj", False),
        ("AB1asdfghj", False),
        ("a1@asdfghj", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    result = check_password(password)
    assert result == expected_result
