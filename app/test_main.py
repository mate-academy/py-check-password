import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "new_input,expected_output",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word", False),
        ("Pass@1", False),
        ("Password1", False),
        ("pass@word1", False),
        ("Pass@word1dfjsldfjlaskjdflsasdl", False)
    ]
)
def test_valid_password(new_input: str, expected_output: bool) -> None:
    assert check_password(new_input) is expected_output
