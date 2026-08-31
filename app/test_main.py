import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "value,expected",
    [
        ("PassWord_#", False),
        ("123456789", False),
        ("qweRty123", False),
        ("Pass@word166", True),
        ("Str@ng", False),
        ("PASword12f434", False),
        ("@pAS12", False),
        ("sword45_@&-66", False),
        ("Pa$s@_word66" * 4, False)
    ]
)
def test_check_password(value: str, expected: bool) -> None:
    assert check_password(value) == expected
