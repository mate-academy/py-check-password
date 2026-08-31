import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "string_to_check, result",
    [
        ("qwerty", False),
        ("qwert!1slo", False),
        ("BasilioЮа1991", False),
        ("killBoy`55", False),
        ("Str@ng1", False),
        ("Str@ngolg", False),
        ("ParalepipedoAlgeb@2024", False),
        ("Pass@word1", True),
        ("Paralepipedo@201", True),
    ],
    ids=[
        "shortness then 8, not use uper, number",
        "not use upper",
        "use UA letter",
        "wrong special character",
        "to short",
        "not use digits",
        "to long",
        "all request respected",
        "all request respected",
    ]
)
def test_check_password_input(string_to_check: str,
                              result: bool) -> None:
    assert (
        check_password(string_to_check) == result
    )
