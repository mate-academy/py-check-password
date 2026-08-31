import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,validation",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("fahs#wohd4", False),
        ("Skijnk9jhg@ljihrqsa", False),
        ("A1_", False),
        ("Lokfe!po", False),
        ("Pokjiy7pl", False)
    ]
)
def test_check_password(password: str, validation: bool) -> None:
    assert check_password(password) == validation


if __name__ == "__main__":
    pytest.main()
