import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("asdfghj", False),
        ("Asdfg1!hj", True),
        ("asd", False),
        ("!!!2222", False),
        ("asdfghjaa!2Asasas", False),
        ("222222222", False),
        ("Aas!a12", False),
        ("trtas!a12", False),
        ("Aasdfda12", False),
        ("Aas!adfdsa", False),
    ]
)
def test_check_password(test_input: str, expected: bool) -> None:
    assert check_password(test_input) == expected


if __name__ == "__main__":
    test_check_password()
