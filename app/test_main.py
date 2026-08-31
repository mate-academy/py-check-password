import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "initial_word, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False,),
        ("Participayd", False),
        ("128567941654", False),
        ("_-#!$571235", False),
        ("Word576164", False),
        ("World#$__!@", False),
        ("Wordla123!@#$987fooD", False),
        ("S@t1a_r", False)
    ]
)
def test_check_password(
        initial_word: str,
        expected_result: bool,
) -> None:
    assert check_password(initial_word) == expected_result
