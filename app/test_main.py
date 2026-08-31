import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        ("Abcdefg@"),
        ("Abcdefg1"),
        ("abcdefg1@"),
        ("Abcdefg1@*"),
        ("Ab1@bbb"),
        ("Ab1@Ab1@Ab1@Ab1@A")
    ]
)
def test_should_return_false_if_password_has_not_any_element(
        password: str,
) -> None:
    assert (check_password(password)) is False
