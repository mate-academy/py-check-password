import pytest
import datetime
# from unittest import mock

from app.main import check_password

GGG = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    }]


@pytest.mark.parametrize(
    "current_rate, predicted_exchange, result", [
        ("Pass@word1", datetime.date(2022, 2, 11), True),
        ("Pass@word", datetime.date(2022, 2, 11), False),
        ("qwerty", datetime.date(2022, 2, 9), False),
        ("qwerty1@", datetime.date(2022, 2, 9), False),
        ("Str@ng1", datetime.date(2022, 2, 10), False),
        ("Str@ñg111", datetime.date(2022, 2, 10), False),
        ("Str@ng∙1", datetime.date(2022, 2, 10), False),
        ("Pass@1", datetime.date(2022, 2, 11), False),
        ("Pass@15648795648dqffwg4", datetime.date(2022, 2, 11), False)

    ]
)
def test_get_exchange_rate_prediction_with_mock(current_rate: str,
                                                predicted_exchange: datetime,
                                                result: bool) -> None:
    predicted_exchange = predicted_exchange

    # with mock.patch("app.main.datetime") as mock_func:
    #     mock_func.date.today.return_value = predicted_exchange
    assert check_password(current_rate) == result
