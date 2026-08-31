import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param(
            "@wer1yU",
            False,
            id="should return False if password too short"
        ),
        pytest.param(
            "@wer1yUiopasdfghj",
            False,
            id="should return False if password too long"
        ),
        pytest.param(
            "qwer1yUiop",
            False,
            id="should return False if password not contains special character"
        ),
        pytest.param(
            "@wertyUiop",
            False,
            id="should return False if password not contains number"
        ),
        pytest.param(
            "@wer1yuiop",
            False,
            id="should return False if password not contains uppercase letter"
        ),
        pytest.param(
            "@wer1yUiop",
            True,
            id="should return True if password match all requirements"
        )
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    result = check_password(password)

    assert result == expected_result
