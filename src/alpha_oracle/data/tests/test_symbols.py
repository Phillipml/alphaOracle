import pytest
from alpha_oracle.data.symbols import BR_SYMBOLS, ALL_BR_SYMBOLS


def test_br_symbols_has_expected_keys():
    assert "indexes" in BR_SYMBOLS
    assert "blue_chips" in BR_SYMBOLS
    assert "diversification" in BR_SYMBOLS


def test_all_br_symbols_not_empty():
    assert len(ALL_BR_SYMBOLS) > 0
    assert isinstance(ALL_BR_SYMBOLS, list)


def test_all_br_symbols_are_strings():
    for s in ALL_BR_SYMBOLS:
        assert isinstance(s, str), f"esperando str e veio {type(s)}"


def test_bvps_are_in_index():
    assert "^BVSP" in BR_SYMBOLS["indexes"]


def test_petr4_andvale3_are_in_blue_chips():
    assert "PETR4.SA" in BR_SYMBOLS["blue_chips"]
    assert "VALE3.SA" in BR_SYMBOLS["blue_chips"]
