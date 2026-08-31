import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "input_pass,expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="test valid password"
        ),
        pytest.param(
            "P@s4d",
            False,
            id="test len less than 8"
        ),
        pytest.param(
            "P@s4d_and_very_long_password",
            False,
            id="test len higher than 17"
        ),
        pytest.param(
            "P@s4ord_Ex@ct_16",
            True,
            id="test len is 16"
        ),
        pytest.param(
            "Pass*■wor{│}d1",
            False,
            id="test contains unsupported chars"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="test not contains digits"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="test not contains uppercase"
        ),
        pytest.param(
            "Password1",
            False,
            id="test not contains special char"
        )
    ]
)
def test_password(input_pass: str, expected_result: bool) -> None:
    assert check_password(input_pass) == expected_result
