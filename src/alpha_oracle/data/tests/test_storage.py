import pytest
import pandas as pd
import tempfile
from pathlib import Path

from alpha_oracle.data.storage import get_data_path, save_data, load_data


def test_get_data_path_return_path():
    path = get_data_path()
    assert isinstance(path, Path)


def test_save_and_load_csv_roundtrip():
    df = pd.DataFrame(
        {"Close": [100.0, 101.0], "Volume": [1000, 1100]},
        index=pd.DatetimeIndex(["2024-01-01", "2024-01-02"]),
    )
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "test.csv"
        save_data(df, str(path))
        assert path.exists()
        loaded = load_data(str(path))
        pd.testing.assert_frame_equal(loaded, df)


def test_save_and_load_parquet_roundtrip():
    df = pd.DataFrame(
        {"Close": [100.0], "Volume": [500]},
        index=pd.DatetimeIndex(["2024-01-01"]),
    )
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "test.parquet"
        save_data(df, str(path))
        loaded = load_data(str(path))
        pd.testing.assert_frame_equal(loaded, df)


def test_save_data_dataframe_empty_error():
    with pytest.raises(ValueError):
        save_data(pd.DataFrame(), "file.csv")
