import pytest

from app.main import check_password


class TestCheckPassword:
    def test_should_check_non_rate_argument(self) -> None:
        with pytest.raises(TypeError):
            check_password(None)

    @pytest.mark.parametrize(
        "password,is_valid",
        [
            pytest.param(
                "AaBb12!",
                False,
                id="test short"
            ),
            pytest.param(
                "AaBb12!-",
                True,
                id="test everything ok"
            ),
            pytest.param(
                "AaBb12!-CcDd",
                True,
                id="test everything ok (more symbols)"
            ),
            pytest.param(
                "AaBb12!-CcDd34567",
                False,
                id="test everything ok (such more symbols)"
            ),
            pytest.param(
                "AaBb12Cc",
                False,
                id="test without special symbols"
            ),
            pytest.param(
                "AaBb!-Cc",
                False,
                id="test without digits symbols"
            ),
            pytest.param(
                "AA12!-CC",
                True,
                id="test without lower latin alphabet symbols"
            ),
            pytest.param(
                "aa12!-cc",
                False,
                id="test without upper latin alphabet symbols"
            )
        ]
    )
    def test_check_correct_result(self, password: str, is_valid: bool) -> None:
        assert check_password(password) == is_valid
