import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Pass$word1", True),
        ("Pass#word1", True),
        ("Pass&word1", True),
        ("Pass!word1", True),
        ("Pass-word1", True),
        ("Pass_word1", True),
        ("Password1", False),
        ("Pass_word", False),
        ("pass_word1", False),
        ("pаss_word1", False),
        ("P_1pppp", False),
        ("P_1ppppp", True),
        ("P_1ppppppppppppp", True),
        ("P_1pppppppppppppp", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
