import yfinance as yf
import pandas as pd
from typing import List, Union


def fetch_market_data(
    symbols: Union[str, List[str]], start: str, end: str
) -> pd.DataFrame:

    try:
        if isinstance(symbols, str):
            symbols = [symbols]

        if not symbols:
            raise ValueError("Lista de símbolos não pode estar vazia")

        data = yf.download(
            symbols,
            start=start,
            end=end,
            group_by="ticker",
            auto_adjust=True,
            progress=False,
            show_errors=False,
        )

        if data.empty:
            print(
                f"Aviso: Nenhum dado enconytrado para {symbols} no período de {start} e {end}"
            )

            return pd.DataFrame()

        return data

    except ValueError as e:
        print(f"Erro de validação: {e}")

    except Exception as e:
        print(f"Erro ao buscar dados de mercado: {e}")
        return pd.DataFrame()
