import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_password",
    [
        ("ab-3cdeFgh", True),
        ("12345678", False),
        ("kndfsa_123JHKHKASDBJHBAD", False),
        ("s9_asIU", False),
        ("kl&sd+$", False),
        ("qwertyuiop", False),
        ("ksdfUUHU_ao", False),
        ("wer_23moien", False),
        ("", False),
        ("lkm8923KJAOJ", False)

    ]
)
def test_check_password(password: str,
                        expected_password: bool,
                        ) -> None:
    assert check_password(password) == expected_password
