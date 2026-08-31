import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("qwertyfirstA$", False),
        ("123456firstA", False),
        ("123456first$", False),
        ("firstsecond$", False),
        ("Str@ng3", False),
        ("Pass@word1Pass@word1", False),
        ("qwertyqwertyA", False),
        ("qwertyqwertyA1$", True),
    ]
)
def test_get_result(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    )


def test_incorrect_data() -> None:
    with pytest.raises(TypeError):
        check_password(4)
