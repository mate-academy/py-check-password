import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("S2@rt", False),
        ("LongerTh@n17letters", False),
        ("sm@llletters1", False),
        ("NoNumbers!", False),
        ("NoSpec1alSymb0ls", False),
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
