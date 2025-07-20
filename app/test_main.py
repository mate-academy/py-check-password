import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_, output",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word1Pass@word1Pass@word1", False),
        ("pass@word1", False),
        ("Passwword1", False),
        ("Pass@1", False),
        ("Abc@dfgerg", False)
    ]
)
def test_main_func(input_: str, output: bool) -> None:
    assert check_password(input_) == output
