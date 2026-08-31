import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "tested_password, expected_result",
    [
        pytest.param("Pass@word1", True,
                     id="Should return true"),
        pytest.param("Ffg!123", False,
                     id="test_should_check_min_length"),
        pytest.param("Fdf!13dfgdfg12312123321123", False,
                     id="test_should_check_max_length"),
        pytest.param("fbcdfgd!1234", False,
                     id="test_should_check_upper_letter"),
        pytest.param("Afgdf!abcd", False,
                     id="test_should_check_digins"),
        pytest.param("Aas45asdasasd", False,
                     id="test_should_check_special_symbols"),
    ]
)
def test_check_password(
    tested_password: str,
    expected_result: bool
) -> None:
    assert check_password(tested_password) == expected_result
