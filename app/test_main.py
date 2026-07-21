from .main import check_password


class TestCheckPassword:
    """Test cases for the check_password function."""

    def test_valid_password(self) -> None:
        """Test that a valid password returns True."""
        assert check_password("Pass@word1") is True

    def test_too_short_password(self) -> None:
        """Test that passwords shorter than 8 characters return False."""
        assert check_password("qwerty") is False
        assert check_password("Abc1!") is False
        assert check_password("") is False

    def test_too_long_password(self) -> None:
        """Test that passwords longer than 16 characters return False."""
        assert check_password("VeryLongPassword123!") is False
        assert check_password("ThisIsTooLongPassword123!") is False

    def test_exact_minimum_length(self) -> None:
        """Test that exactly 8 characters can be valid."""
        assert check_password("Abc1!def") is True

    def test_exact_maximum_length(self) -> None:
        """Test that exactly 16 characters can be valid."""
        assert check_password("Abc1!defghijklmn") is True

    def test_missing_uppercase(self) -> None:
        """Test that passwords without uppercase letters return False."""
        assert check_password("pass@word1") is False
        assert check_password("str@ng") is False

    def test_missing_digit(self) -> None:
        """Test that passwords without digits return False."""
        assert check_password("Pass@word") is False
        assert check_password("Abcdef!g") is False

    def test_missing_special_character(self) -> None:
        """Test that passwords without special characters return False."""
        assert check_password("Password1") is False
        assert check_password("Abcdefg1") is False

    def test_invalid_characters(self) -> None:
        """Test that passwords with invalid characters return False."""
        assert check_password("Pass@word1%") is False
        assert check_password("Pass@word1*") is False
        assert check_password("Pass@word1+") is False
        assert check_password("Pass@word1 ") is False
        assert check_password("Pass@word1\n") is False

    def test_non_latin_characters(self) -> None:
        """Test that non-Latin characters are rejected."""
        assert check_password("Pass@word1а") is False
        assert check_password("Pass@word1é") is False
        assert check_password("Pass@word1ñ") is False

    def test_allowed_special_characters(self) -> None:
        """Test that all allowed special characters work."""
        assert check_password("Pass$word1") is True
        assert check_password("Pass@word1") is True
        assert check_password("Pass#word1") is True
        assert check_password("Pass&word1") is True
        assert check_password("Pass!word1") is True
        assert check_password("Pass-word1") is True
        assert check_password("Pass_word1") is True

    def test_multiple_special_characters(self) -> None:
        """Test that multiple special characters are allowed."""
        assert check_password("Pass@#$word1") is True
        assert check_password("Pass!@#$%^&*()") is False  # Some invalid chars

    def test_edge_cases(self) -> None:
        """Test various edge cases."""
        # All special characters
        assert check_password("Abcdefg1$") is True
        assert check_password("Abcdefg1@") is True
        assert check_password("Abcdefg1#") is True
        assert check_password("Abcdefg1&") is True
        assert check_password("Abcdefg1!") is True
        assert check_password("Abcdefg1-") is True
        assert check_password("Abcdefg1_") is True

        # Mixed case with numbers and special chars
        assert check_password("aBc1!dEf") is True
        assert check_password("1Abc!def") is True
        assert check_password("!Abc1def") is True

    def test_boundary_lengths(self) -> None:
        """Test boundary conditions for length."""
        # 7 characters (too short)
        assert check_password("Abc1!d") is False
        # 8 characters (minimum)
        assert check_password("Abc1!def") is True
        # 16 characters (maximum)
        assert check_password("Abc1!defghijklmn") is True
        # 17 characters (too long)
        assert check_password("Abc1!defghijklmno") is False
