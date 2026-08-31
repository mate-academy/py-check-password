import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("Pass@word", False),
        ("Pass@word1andonemorepassword", False),
        ("pass@word1", False),
        ("Pass@1", False),
        ("Password1", False)
    ],
    ids=[
        "all rules are met - True",
        "password without digits - False",
        "too long password - False",
        "password without uppercase letter - False",
        "short password - False",
        "password without specail symbols - False"
    ]
)
def test_outdated_products(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
