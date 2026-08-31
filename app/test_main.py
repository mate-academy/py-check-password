import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_output",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="should return `True` when password='Pass@word1'"
        ),
        pytest.param(
            "7Char$$",
            False,
            id="should return `False` when password='7Char$$'"
        ),
        pytest.param(
            "17_Chars_string#!",
            False,
            id="should return `False` when password='17_Chars_string#!'"
        ),
        pytest.param(
            "NoDigit$string",
            False,
            id="should return `False` when password='NoDigit$string'"
        ),
        pytest.param(
            "no-upp3rcs$e",
            False,
            id="should return `False` when password='no_upp3rcs$e'"
        ),
        pytest.param(
            "NoSpec1alChrs",
            False,
            id="should return `False` when password='NoSpec1alChrs'"
        ),
        pytest.param(
            "Unsupp0rted©hr",
            False,
            id="should return `False` when password='Unsupp0rted©hr'"
        )
    ]
)
def test_check_password(password, expected_output):
    assert check_password(password) is expected_output
