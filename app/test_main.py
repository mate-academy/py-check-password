import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "input_data, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("DDDbbbhhh12345", False),
        ("Sgfdhji_e12345678n", False),
        ("gdf6-vb-f", False),
        ("adSfgdfh!", False),
        ("FF44e_d", False)
    ]
)
def test_password_check(
        input_data: str,
        expected_result: bool
) -> None:
    assert check_password(input_data) == expected_result
