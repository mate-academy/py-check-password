# write your code here
import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        (
            'Pass@word1adsasddasadsads',
            False
        ),
        (
            'Test1ahsdh',
            False
        ),
        (
            'testPass$',
            False
        ),
        (
            'testpass1$',
            False
        ),
        (
            'Test1%ij',
            False
        )
    ]
)
def test_correct_function_work(password, expected):
    assert check_password(password) == expected


def test_for_short_pass():
    assert not check_password("tesT1$")
