from typing import Type

import pytest

from app.main import check_password


class TestCheckPasswordClass:
    @pytest.mark.parametrize(
        "password, excepted", [
            ("Pass@word1", True),
            ("@wer1yU", False,),
            ("Str@ng", False),
            ("S12fdghjklzxcbn@nm", False),
            ("іваулІ234", False),
            ("pass@word1", False),
            ("@wertyUiop", False)
        ],
        ids=[
            "good password",
            "should return False if password too short",
            "returns False for short passwords",
            "very long",
            "not latin alphabet Aa-Zz",
            "returns False for passwords without uppercase letter",
            "returns False for passwords without digits"
        ]
    )
    def test_check_password(self,
                            password: str,
                            excepted: bool
                            ) -> None:
        assert check_password(password) == excepted


class TestExpectedError:
    @pytest.mark.parametrize(
        "password, expected_error",
        [
            pytest.param(
                5,
                TypeError,
                id="should raise TypeError if current_rate is not str"
            ),
        ]
    )
    def test_raising_correctly(
            self,
            password: str,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            check_password(password)
