import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Abc@1234", True),
        ("A1b@Cdef", True),
        ("Abc12345", False),
        ("Abc@Defgh", False),
        ("abc@1234", False),
        ("Abc!@#$%", False),
        ("A1b@CdEfGhIjKlmNOP", False),
        ("A1b@CdEfGhIjKlmNOP1I234J", False),
        ("A1c@t", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
