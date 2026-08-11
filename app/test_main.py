import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password_to_check, check_password_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Strong123", False),
        ("Strong!@#", False),
        ("strong12#", False),
        ("Strong12345!@#$-", True),
        ("Strong12345!@#$-_", False),
        ("", False),
        ("Strng!1", False),
    ],
    ids=[
        "Test check correct password",
        "Test check password, len of password less than 8 characters",
        "Test check password, len of password less than 8 characters",
        "Test check password without special symbols",
        "Test check password without digits",
        "Test check password without characters in upper case",
        "Test check correct password with len equal to 16 characters",
        "Test check correct password with len equal to 17 characters",
        "Test check empty password",
        "Test check correct password with len equal to 7 characters"
    ]
)
def test_check_password(
        password_to_check: str,
        check_password_result: bool
) -> None:
    assert (check_password(password_to_check) == check_password_result), \
        (f"Password \'{password_to_check}\' "
         f"should be accepts only letters of the Latin alphabet Aa-Zz, "
         f"digits 0-9 or special character from $@#&!-_, "
         f"contains at least 1 digit, 1 special character, "
         f"one upper case letter and has length from 8 to 16 characters")
