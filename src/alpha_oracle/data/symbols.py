BR_SYMBOLS = {
    "indexes": [
        "^BVSP",  # IBOVESPA
    ],
    "blue_chips": [
        "PETR4.SA",  # Petrobras PN
        "VALE3.SA",  # Vale ON
        "ITUB4.SA",  # Itaú PN
        "BBDC4.SA",  # Bradesco PN
        "ABEV3.SA",  # Ambev
        "WEGE3.SA",  # WEG
        "RENT3.SA",  # Localiza
        "BBAS3.SA",  # Banco do Brasil
        "RAIL3.SA",  # Rumo (logística)
        "ELET3.SA",  # Eletrobras
    ],
    "diversification": [
        "MGLU3.SA",  # Varejo/Magazine
        "VIVT3.SA",  # Telecom
        "CSNA3.SA",  # Siderurgia
        "CYRE3.SA",  # Construção
        "SBSP3.SA",  # Saneamento
        "EQTL3.SA",  # Energia
    ],
}
ALL_BR_SYMBOLS = (
    BR_SYMBOLS["indexes"] + BR_SYMBOLS["blue_chips"] + BR_SYMBOLS["diversification"]
)
