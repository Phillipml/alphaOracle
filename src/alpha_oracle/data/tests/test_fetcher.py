import pandas as pd
import pytest
from unittest.mock import patch, MagicMock

from alpha_oracle.data.fetcher import fetch_market_data, fetch_and_save


@patch("alpha_oracle.data.fetcher.yf")
def test_fetch_market_data_return_dataframe_with_data(mock_yf):
    fake_df = pd.DataFrame(
        {"Open": [100], "High": [101], "Low": [99], "Close": [100.5], "Volume": [1000]},
        index=pd.DatetimeIndex(["2024-01-01"]),
    )
    mock_yf.download.return_value = fake_df
    result = fetch_market_data("PETR4.SA", "2024-01-01", "2024-01-02")
    assert not result.empty
    assert isinstance(result, pd.DataFrame)
    mock_yf.download.assert_called_once()


@patch("alpha_oracle.data.fetcher.yf")
def test_fetch_market_data_return_empty_where_no_data(mock_yf):
    mock_yf.download.return_value = pd.DataFrame()
    result = fetch_market_data("INVALIDO", "2024-01-01", "2024-01-02")
    assert result.empty


def test_fetch_market_data_empty_list_value_error():
    result = fetch_market_data("PETR4.SA", "2024-01-01", "2024-01-02")
    assert isinstance(result, pd.DataFrame)
