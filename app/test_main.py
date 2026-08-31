import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "tested_password, expected_result",
    [
        pytest.param("1sfgryhfcdgnngcjgfdvd", False),
        pytest.param("arcRvhf", False),
        pytest.param("Pasй@word1", False),
        pytest.param("qwertyrt", False),
        pytest.param("Pass@word1", True)

    ],
    ids=[
        "should have maximum 16 characters",
        "should have minimum 8 characters",
        "accepts only letters of the Latin alphabet",
        "should contains at least 1 digit, 1 special, 1 uppercase.",
        "should be valid password"
    ]
)
def test_should_check_if_password_valid(
        tested_password: str,
        expected_result: bool
) -> None:
    assert check_password(tested_password) == expected_result
