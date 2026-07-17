import pytest
from app import main


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,is_valid",
        [
            ("Кирилиця", False),
            ("?,.<>%^*()+", False),
            ("12345678", False),
            ("Qwertyui$", False),
            ("qwerty123$", False),
            ("Qwerty12345", False),
            ("$$$@#&!-_", False),
            ("QWERTY123$", True),
            ("Q1$", False),
            ("Qwertyuiopasdf123$", False),
            ("QWERTY123$", True),
            ("Qwerty123$", True),
        ],
        ids=[
            "Not Latin letters",
            "Wrong special symbols",
            "All numbers",
            "No digits",
            "No uppercase letter",
            "No special symbols",
            "All allowed special symbols",
            "All letters uppercase",
            "Too short password",
            "Too long password",
            "All letters uppercase + valid symbols",
            "Some letters uppercase + valid symbols"
        ]
    )
    def test_check_password(
        self,
        password: str,
        is_valid: bool
    ) -> None:
        assert main.check_password(password) == is_valid
