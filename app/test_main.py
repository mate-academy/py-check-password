import pytest
from app.main import check_password


class TestMain:
    @pytest.mark.parametrize(
        "password, expected",
        [
            ("P@ss1", False),
            ("Pass@1ab", True),
            ("P@ssw0rd123", True),
            ("P@ssword1234ABCD", True),
            ("P@ssword1234ABCDE", False),
            ("Password@", False),
            ("Password1", False),
            ("password1@", False),
            ("P@ssword1*", False),
            ("Pass@word1", True),
            ("Password", False),
            ("A1@a", False),
            ("Abcdefg1@", True),
            ("Abcdefghijklmno1@", False),
            ("Abcdefghijklmnop1@", False),
        ],
        ids=[
            "less_than_8_chars",
            "exactly_8_chars_valid",
            "between_8_and_16_chars_valid",
            "exactly_16_chars_valid",
            "more_than_16_chars",
            "missing_digit",
            "missing_special_char",
            "missing_uppercase",
            "invalid_char",
            "all_valid_conditions",
            "only_letters_no_requirements",
            "less_than_8_chars_invalid",
            "exactly_8_chars_valid_edge",
            "exactly_16_chars_valid_edge",
            "more_than_16_chars_invalid_edge",
        ]
    )
    def test_should_check_password_correctly(
            self,
            password: str,
            expected: bool,
    ) -> None:
        assert check_password(password) == expected
