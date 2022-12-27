import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param("Pass@word1@", True, id="password is correct"),
        pytest.param("Sho1@", False, id="should_check_min_length"),
        pytest.param(
            "V1@erylonglonglonglongpassword",
            False,
            id="should_check_max_length"
        ),
        pytest.param(
            "noupperletters1@",
            False,
            id="should_check_upper_letter"
        ),
        pytest.param("N@odigits", False, id="should_check_digit"),
        pytest.param("nospecsymbols", False, id="should_check_special_symbols")
    ]
)
def test_check_password(
        password: str,
        expected_result: bool) -> None:
    assert check_password(password) == expected_result
