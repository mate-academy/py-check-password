import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_pass, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("1Qazw@sxed", True),
        ("1Qazwtyui$1234", True),
        ("1azwtyui$1234g", False),
        ("1Qazwtyui$1234gwq1", False),
        ("Qazw@tyui$g", False),
        ("1Q$", False),
        ("1Qazwrtyui123g", False)
    ]
)
def test_check_password(input_pass: str, expected_result: bool) -> None:
    assert check_password(input_pass) == expected_result
