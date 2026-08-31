import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwF1@", False),
        ("12345Dfff#$jjjjkvfrhnn546", False),
        ("pass@word1", False),
        ("Passaword1", False),
        ("Pass@wordd", False)

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
