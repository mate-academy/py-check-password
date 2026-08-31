import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, expected_bool_value",
        [
            pytest.param(
                "S@ms4ng",
                False,
                id="password length should be greater then 7 words"
            ),
            pytest.param(
                "S@ms4ng8901234567",
                False,
                id="password length should be less then 18 words"
            ),
            pytest.param(
                "samsung_s_22",
                False,
                id="password must contain at least one capital letter"
            ),
            pytest.param(
                "Самсунг_s_22",
                False,
                id="password must contain only letters of the English alphabet"
            ),
            pytest.param(
                "Samsung_s_twenty_two",
                False,
                id="password must contain at least one number"
            ),
            pytest.param(
                "Samsung_s.22",
                False,
                id="password must contain at least "
                   "one special symbol ($@#&!-_)"
            ),
            pytest.param(
                "Samsung_s_22",
                True,
                id="should return True if password is right"
            )
        ]
    )
    def test_check_password_valid_password(
            self,
            password: str,
            expected_bool_value: bool
    ) -> None:
        assert check_password(password) is expected_bool_value

    def test_raises_type_error_if_password_is_not_string(self) -> None:
        with pytest.raises(TypeError):
            check_password(123456789)
