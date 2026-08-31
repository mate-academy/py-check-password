import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("weak", False),
        ("weakweak", False),
        ("Weakweakweakweak1@", False),
        ("Weakweak1@фон", False),
        ("Weakweak@", False),
        ("Weakweak1", False),
        ("weakweak1@", False),
        ("Weakweak1@", True)
    ],
    ids=[
        "less then 8 characters",
        "8 characters only lowercase",
        "more then 16 characters",
        "contain non latin character",
        "don't contain digit",
        "don't contain special character ($@#&!-_;)",
        "don't contain uppercase character",
        "valid password"
    ]
)
def test_can_sum(password: str, result: bool) -> None:
    assert (check_password(password) == result),\
        f"Return of func for password={password} should be equal to {result}"
