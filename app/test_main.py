import pytest

from app.main import check_password


class TestCheckIncorrectPasswords:
    @pytest.mark.parametrize(
        "password",
        [
            pytest.param(
                "Qwwerrsty7982340572",
                id=("test should return false if more then 9 digits")
            ),
            pytest.param(
                "Qt@s1",
                id=("test should return false for short passwords")
            ),
            pytest.param(
                "Qwertiyue",
                id=("test should return false if only letters")
            ),
            pytest.param(
                "1234568q@",
                id=("test should return false if no uppercase letter")
            ),
            pytest.param(
                "1234568hajkdsk@gH",
                id=("test should return false if more then 16 characters")
            ),
            pytest.param(
                "123425привет",
                id=("test should return false if no latin letters")
            ),
            pytest.param(
                "Strssi5ng",
                id=("test should return false without special symbols")
            ),
            pytest.param(
                "Strssi!ng",
                id=("test should return false without digits")
            ),
        ]
    )
    def test_should_return_false(self, password: str) -> None:
        assert check_password(password) is False


class TestCheckCorrectPasswords:
    @pytest.mark.parametrize(
        "password",
        [
            (
                "Qwwerty1!"
            ),
            (
                "Qwessdrty2@"
            ),
            (
                "Strssi5!ng"
            ),
            (
                "123456789q@Q"
            ),
            (
                "123456789qqjhf@Q"
            ),
        ]
    )
    def test_should_return_true(self, password: str) -> None:
        assert check_password(password) is True
