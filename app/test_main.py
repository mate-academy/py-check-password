import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "has_upper_digit_special, expected_result",
        [
            ('Str2gdfdf', False),
            ('Str@ngdss', False),
            ('dass@word1', False),
            ('Das@wo1', False),
            ('Dass@word1asdfghjj', False),
        ]
    )
    def test_check_password(self,
                            has_upper_digit_special,
                            expected_result):
        assert check_password(has_upper_digit_special) == expected_result
