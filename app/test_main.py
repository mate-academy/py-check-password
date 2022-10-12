import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "input_value, expected",
        [pytest.param(
            "Pass@word1",
            True,
            id="Should return True if password is 'Pass@word1'"),
         pytest.param(
            "whitoutupp1!",
            False,
            id="Should return True if password is 'whitoutupp1!'"),
         pytest.param(
            "W2@",
            False,
            id="Should return True if password is 'W2@'"),
         pytest.param(
            "Withoutdigt!@",
            False,
            id="Should return True if password is 'Withoutdigt!@'"),
         pytest.param(
            "Str@ng",
            False,
            id="Should return True if password is 'Str@ng'"),
         pytest.param(
            "Ihavemorethan@!16",
            False,
            id="Should return True if password is 'Ihavemorethan@!16'"),
         ]
    )
    def test_check_password(self,
                            input_value: str,
                            expected: bool
                            ) -> None:
        assert check_password(input_value) == expected
