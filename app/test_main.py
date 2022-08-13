import pytest

from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "actual,expected",
        [
            pytest.param("Pass@word1", True, id="valid 1"),
            pytest.param("Qwerty123@#$", True, id="valid 2"),
            pytest.param("_###ABC123$$$_", True, id="valid 3"),
            pytest.param("#ABC123", False, id="too short"),
            pytest.param("ABCD12345", False, id="without specs"),
            pytest.param("AbCd_EfGhEi", False, id="without numbers"),
            pytest.param("_@#$!!123___", False, id="without chars"),
            pytest.param("_0VeryVeryLongPass!!!", False, id="very long"),
        ]
    )
    def test_check_password(self, actual, expected):
        assert check_password(actual) == expected
