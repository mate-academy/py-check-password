import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1",
         True),
        ("qwerty",
         False),
        ("Str@ng",
         False),
        ("iyyr@ng@789ngSrng",
         False),
        ("плпррьн",
         False),
        ("jgg@ggJvq",
         False),
        ("ljhgd@2567",
         False),
        ("gjh578LL",
         False),
        ("h_9L",
         False),


    ]
)
def test_should_return_correct_bool(password: str, expected: bool) -> None:
    assert check_password(password) == expected
