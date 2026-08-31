import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, bool_return",
    [
        ("k@A122", False),
        ("hshjhjkhakskkkk12@DD", False),
        ("GHJsjdfnsd@б", False),
        ("Gqa123safbkasj", False),
        ("dsfjfkArtur@", False)
    ]
)
def test_check_password(
        password: str,
        bool_return: bool
) -> None:
    assert check_password(password=password) == bool_return
