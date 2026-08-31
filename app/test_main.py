import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("Qwe7t#", False),
        ("St2r@ngЯW", False),
        ("Df4anime59F14b", False),
        ("SamsungSA19#f24b8", False),
        ("naruto#2&", False),
        ("Probo#uyt", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
