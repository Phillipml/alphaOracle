import pandas as pd
import os
from pathlib import Path
from typing import Optional


def get_data_path() -> Path:
    data_path = os.getenv("DATA_PATH")
    if data_path:
        return Path(data_path)
    project_root = Path(__file__).parent.parent.parent.parent
    return project_root / "data"


def save_data(df: pd.DataFrame, path: str) -> None:
    if df.empty:
        raise ValueError("DataFrame não pode estar vazio")
    file_path = Path(path)

    if not file_path.is_absolute():
        base_path = get_data_path()
        file_path = base_path / file_path

    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.suffix.lower() == ".parquet":
        df.to_parquet(file_path, index=True)
    else:
        df.to_csv(file_path, index=True, date_format="%Y-%m-%d")


def load_data(path: str) -> pd.DataFrame:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado:{file_path}")

    if file_path.suffix.lower() == ".parquet":
        df = pd.read_parquet(file_path)
    elif file_path.suffix.lower() == ".csv":
        df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    else:
        raise ValueError(
            f"Formato não suportado: {file_path.suffix}. Use .csv ou .parquet"
        )

    return df
