import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("", False, id="no_password"),
        pytest.param("aCD#4", False, id="short_password"),
        pytest.param("Abcdefghjka#skdj1", False, id="too_long_password"),
        pytest.param("Abcdskdj1", False, id="no_symbol"),
        pytest.param("abda#skdj1", False, id="no_upper"),
        pytest.param("Abcdefghi#", False, id="no_number"),
        pytest.param("abcdefghijk", False, id="only_low_letters"),
        pytest.param("Abcdef#4", True, id="valid_password"),


    ]
)
def test_password_validation(password: str, result: bool) -> None:
    assert check_password(password) == result
