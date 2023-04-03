import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password, expected",
        [
            pytest.param("Pass@word1", True, id="valid_password_returns_true"),
            pytest.param(
                "Pass@word1^",
                False,
                id="contains_invalid_character"
            ),
            pytest.param(
                "qwer@1Y",
                False,
                id="test_should_check_min_length"
            ),
            pytest.param(
                "Pass@word1truiaj4",
                False,
                id="test_should_check_max_length"
            ),
            pytest.param(
                "Pass@word",
                False,
                id="test_should_check_digit"
            ),
            pytest.param(
                "Password1",
                False,
                id="test_should_check_special_symbols"
            ),
            pytest.param(
                "ass@word1",
                False,
                id="test_should_check_upper_case_letter"
            ),
        ]
    )
    def test_check_password(self, password: str, expected: bool) -> None:
        assert check_password(password) == expected

    def test_should_raise_error_when_input_is_invalid(self) -> None:
        with pytest.raises(TypeError):
            check_password(2)
