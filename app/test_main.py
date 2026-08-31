import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, password_status",
    [
        ("Pass@word1", True),
        ("qwertyui", False),
        ("Str@ng1", False),
        ("Very1ongP@ssword!", False),
        ("passw@rd1", False),
        ("Passw@rd", False),
        ("Password1", False)
    ],
    ids=[
        "uppercase letter, correct length, special symbols, digits",
        "check password with only letters and too short",
        "check too short password",
        "check too long password",
        "check password without uppercase letter",
        "check password without digits",
        "check password without special symbols"
    ]
)
def test_main_cases_for_check_password_function(
    password: str,
    password_status: bool
) -> None:
    assert check_password(password) == password_status


def test_check_password_incorrect_input() -> None:
    with pytest.raises(TypeError):
        check_password(12242)
