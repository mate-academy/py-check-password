import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("Pass@wor1", True),
        ("1234", False),
        ("Qwertyui@", False),
        ("Very_Long_Password123", False),
        ("Str@ng", False),
        ("good_p4ssword", False),
        ("S@41", False),
        ("Qw3rtyui", False)
    ]
)
def test_check_password(
        password: str,
        expected_result: bool,
) -> None:
    assert check_password(password) == expected_result
