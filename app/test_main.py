from pytest import mark

from app.main import check_password


@mark.parametrize(
    "input_password, validation",
    [
        ("Sea12@s", False),
        ("Sea12@sSea12@sSea", False),
        ("Waterfall@", False),
        ("Waterfall1", False),
        ("waterfall@1", False),
        ("Waterfall@1", True)
    ],
    ids=[
        "should return False when length is too short",
        "should return False when length is too long",
        "should return False when no digits",
        "should return False when no special symbols",
        "should return False when no uppercase letters",
        "should return True when all conditions are met"
    ]
)
def test_if_password_validates_correctly(
        input_password: str,
        validation: bool
) -> None:
    assert check_password(input_password) == validation
