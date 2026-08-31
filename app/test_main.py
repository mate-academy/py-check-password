import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_data, expected",
    [
        pytest.param("Pass@word1", True, id="Aa-Zz or 0-9 or $@#&!-_"),
        pytest.param("P@1s", False, id="min 8 characters"),
        pytest.param("Pass@word1Pass@wor", False, id="max 16 characters"),
        pytest.param("p@ssword1", False,
                     id="at least 1 uppercase letter"),
        pytest.param("P@ssword", False,
                     id="at least 1 digit"),
        pytest.param("Password1", False,
                     id="at least 1 special character"),

    ]
)
def test_check_password(input_data: str, expected: bool) -> None:
    assert check_password(input_data) == expected
