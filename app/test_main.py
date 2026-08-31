from pytest import mark, param

from app.main import check_password


@mark.parametrize(
    "password, expected_result",
    [
        param(
            "Qw@r7y", False,
            id="Length should be at least 8 characters"),
        param(
            "Qwertyu1opa$dfghjkl", False,
            id="Length should be maximum 16 characters inclusive"),
        param(
            "P@ssword", False,
            id="Should contains at least 1 digit"),
        param(
            "Password1", False,
            id="Should contains at least 1 special character"),
        param(
            "p@ssword1", False,
            id="Should contains at least 1 uppercase letter"),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) is expected_result
