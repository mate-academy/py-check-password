import pytest
import app.main


@pytest.mark.parametrize(
    "tested_password, expected_result",
    [
        ("$h0rT", False),
        ("P@ssw0rdIsTooLong", False),
        ("p@ssw0rd", False),
        ("P@ssword", False),
        ("Passw0rd", False)
    ],
    ids=[
        "too short password should not be accepted",
        "too long password should not be accepted",
        "password without upper letter should not be accepted",
        "password without digit should not be accepted",
        "password without special character should not be accepted",
    ]
)
def test_check_password(tested_password: str, expected_result: bool) -> None:
    actual_result = app.main.check_password(tested_password)
    assert actual_result is expected_result
