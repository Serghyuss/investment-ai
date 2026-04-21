import pandas as pd
import numpy as np

def calculate_roi(df: pd.DataFrame):
    df["roi"] = (df["valor_atual"] - df["valor_aplicado"]) / df["valor_aplicado"]
    return df


def portfolio_summary(df: pd.DataFrame):
    total_aplicado = df["valor_aplicado"].sum()
    total_atual = df["valor_atual"].sum()

    roi_total = (total_atual - total_aplicado) / total_aplicado

    return {
        "total_aplicado": total_aplicado,
        "total_atual": total_atual,
        "roi_total": roi_total
    }


def risk_metrics(df: pd.DataFrame):
    # Simulação simples (melhorar depois com histórico)
    vol = np.std(df["roi"])

    concentracao = df["valor_atual"] / df["valor_atual"].sum()

    return {
        "volatilidade": float(vol),
        "maior_concentracao": float(concentracao.max())
    }

def classify_risk(volatilidade, concentracao):
    
    if volatilidade > 0.10:
        vol_class = "ALTA"
    elif volatilidade >= 0.05:
        vol_class = "MODERADA"
    else:
        vol_class = "BAIXA"

    if concentracao > 0.40:
        conc_class = "ALTA"
    elif concentracao >= 0.20:
        conc_class = "MODERADA"
    else:
        conc_class = "BAIXA"

    return {
        "volatilidade_class": vol_class,
        "concentracao_class": conc_class
    }

def portfolio_score(roi, vol_class, conc_class):

    score = 100

    # Penalizações
    if roi < 0:
        score -= 30
    elif roi < 0.05:
        score -= 15

    if vol_class == "ALTA":
        score -= 25
    elif vol_class == "MODERADA":
        score -= 10

    if conc_class == "ALTA":
        score -= 20
    elif conc_class == "MODERADA":
        score -= 10

    return max(score, 0)