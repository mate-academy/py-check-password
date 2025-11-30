import pytest
import app.main


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty@420", False),
        ("Str@ng2", False),
        ("Thispass@wordistolong69", False),
        ("Nosymbol88", False),
        ("No_digit", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    test_results = app.main.check_password(password)
    assert test_results == result
