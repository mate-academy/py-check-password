from .main import check_password
import pytest


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word1Pass@wo", False),
        ("Pas@", False),
        ("asdfg6@id", False),
        ("Qwerty@Kq", False),
        ("Password1", False),
        ("Str@nq", False),
        ("dDqfg6qid", False)


    ]
)
def test_check_password(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected
