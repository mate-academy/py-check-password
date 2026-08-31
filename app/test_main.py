import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "example, result",
    [
        ("pass@word1", False),
        ("Pass@word1Pass@word1", False),
        ("Pass@1", False),
        ("Password1", False),
        ("Password@", False),
        ("Pass@word1", True)
    ],
    ids=[
        "Short password",
        "No special character",
        "No uppercase",
        "Incorrect",
        "Incorrect",
        "Incorrect",
    ]
)
def test_check_password(example: str, result: bool) -> None:
    assert check_password(example) == result
