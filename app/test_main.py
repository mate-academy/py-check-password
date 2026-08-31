from pytest import mark, param

from app.main import check_password


@mark.parametrize(
    "password, expected_result",
    [
        param("11qW#", False,
              id="Password should has at least 8 character"),

        param("asaWs121duckduck#####", False,
              id="Password should has maximum 16 characters"),

        param("121_Анна", False,
              id="Password should has only letters of the Latin alphabet "
                 "Aa-Zz, digits 0-9 or special character from $@#&!-_"),

        param("aaaa###QQQQ", False,
              id="Password should has at least 1 digit"),

        param("qawsQAQA819", False,
              id="Password should has at least 1 special character"),

        param("qaws####819", False,
              id="Password should has at least 1 uppercase letter"),

        param("qaws####819AA", True,
              id="Correct password should return True")
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) is expected_result
