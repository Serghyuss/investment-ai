import yfinance as yf

def get_stock_data(ticker: str):

    ticker = ticker.upper()

    # Para Brasil precisa .SA
    if not ticker.endswith(".SA"):
        ticker = f"{ticker}.SA"

    stock = yf.Ticker(ticker)

    info = stock.info
    hist = stock.history(period="6mo")

    return {
        "ticker": ticker,
        "preco_atual": info.get("currentPrice"),
        "nome": info.get("longName"),
        "setor": info.get("sector"),
        "variacao": info.get("regularMarketChangePercent"),
        "historico": hist
    }