import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            'Pass@word1',
            True,
            id="correct password"
        ),
        pytest.param(
            "Q1@s",
            False,
            id="short password"
        ),
        pytest.param(
            'qweWrtyiejfij34#dufjjjdlsioejfenfl',
            False,
            id="too long password"
        ),
        pytest.param(
            'Surutr@ng',
            False,
            id="without digit"
        ),
        pytest.param(
            'Surutrtng1',
            False,
            id="without special symbols"
        ),
        pytest.param(
            '1urutr@ng',
            False,
            id="without upper letter"
        )
    ]
)
def test_check_password(password, expected):
    assert check_password(password) == expected
