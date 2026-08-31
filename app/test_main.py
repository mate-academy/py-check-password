import pytest


from app.main import check_password


class TestIsIsogram:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param(
                "Pass@word1",
                True,
                id="correct password"
            ),
            pytest.param(
                "Dr@gon2",
                False,
                id="password is short"
            ),
            pytest.param(
                "2000Nikor@Dragon2000",
                False,
                id="password is too long"
            ),
            pytest.param(
                "dragon@2000",
                False,
                id="password without uppercase letter'"
            ),
            pytest.param(
                "Dragon2000",
                False,
                id="password without '$@#&!-_'"
            ),
            pytest.param(
                "Dragon@Nikor",
                False,
                id="password without digits"
            )

        ]
    )
    def test_check_password(
            self,
            password: str,
            result: bool
    ) -> None:
        assert check_password(password) == result
