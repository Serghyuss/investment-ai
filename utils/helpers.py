def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_percent(value: float) -> str:
    return f"{value*100:,.2f}%".replace(",", "X").replace(".", ",").replace("X", ".")