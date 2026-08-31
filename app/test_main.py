import pytest
from app.main import check_password


class TestCheckPassword:

    @pytest.mark.parametrize(
        "password, expected_result",
        [
            ('Pass@word1', True),
            ('qwerty', False),
            ('Str@ng', False),
            ('P@1s', False),
            ('S0meverrrylongP@s', False),
            ('', False)
        ]
    )
    def test_should_return_valid_value(self, password, expected_result):
        assert check_password(password) == expected_result
