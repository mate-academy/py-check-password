import pytest


from app.main import check_password


@pytest.mark.parametrize("value,expected", [
    ("паролб5555[]", False),
    ("' - - - -)(", False),
    ("Pass@word1", True)
])
def test_password_should_contain_valid_symbols(value: str,
                                               expected: bool
                                               ) -> None:
    assert check_password(value) == expected


@pytest.mark.parametrize("value,expected", [
    ("12W4!67", False),
    ("123456789@bcDefgh", False),
    ("K1ndaCoolP@sswrd", True)
])
def test_password_must_be_8_16_range(value: str,
                                     expected: bool
                                     ) -> None:
    assert check_password(value) == expected


@pytest.mark.parametrize("value,expected", [
    ("P@ssword", False),
    ("pASSword1", False),
    ("p@ssword1", False)
])
def test_must_contain_at_least(value: str,
                               expected: bool
                               ) -> None:
    assert check_password(value) == expected
