import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def preprocess(df: pd.DataFrame):

    # 🔍 Validação de colunas
    required_cols = ["ativo", "quantidade", "preco_medio", "preco_atual"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {col}")

    # 🔹 Conversão de tipos
    df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
    df["preco_medio"] = pd.to_numeric(df["preco_medio"], errors="coerce")
    df["preco_atual"] = pd.to_numeric(df["preco_atual"], errors="coerce")

    # 🔹 Cálculos
    df["valor_aplicado"] = df["quantidade"] * df["preco_medio"]
    df["valor_atual"] = df["quantidade"] * df["preco_atual"]

    # 🔹 Limpeza
    df = df.dropna()

    return df