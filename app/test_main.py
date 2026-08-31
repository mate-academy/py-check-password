from pytest import mark, param


from app.main import check_password


@mark.parametrize(
    "password, expected_result",
    [
        param(
            "Qwert_1", False,
            id="Should return False when password has less than 8 characters"
        ),
        param(
            "SuperStrongPassword_123", False,
            id="Should return False when password has more than 16 characters"
        ),
        param(
            "Strong_Password", False,
            id="Should return False when password has no numbers"
        ),
        param(
            "1DigitandLetters", False,
            id="Should return False when password has no special characters"
        ),
        param(
            "1digit_letters", False,
            id="Should return False when password has no uppercase letters"
        ),
        param(
            "Cool_password42", True,
            id="Should return True when password is ok"
        )
    ]
)
def test_check_password_correctly(
    password: str,
    expected_result: bool
) -> None:
    assert check_password(password) == expected_result
