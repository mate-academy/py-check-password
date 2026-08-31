import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("HotD$g123", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("HdjQdQdd098jdn!DfHhJK", False),
        ("", False),
        ("qwert#y123", False),
        ("Qwetry5try", False),
        ("Qwetrytry123", False),
        ("F8!", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
