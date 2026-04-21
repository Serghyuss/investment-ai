from modules.ingestion.parser import load_csv, preprocess
from modules.analytics.engine import (
    calculate_roi,
    portfolio_summary,
    risk_metrics,
    classify_risk,
    portfolio_score
)
from modules.llm.llm_client import generate_analysis


def run_pipeline(file_path: str):

    # 🔹 1. Ingestão
    df = load_csv(file_path)
    df = preprocess(df)

    # 🔹 2. Cálculos
    df = calculate_roi(df)
    summary = portfolio_summary(df)
    risk = risk_metrics(df)

    # 🔹 3. Regras determinísticas
    if risk["maior_concentracao"] > 0.4:
        alerta = "Alta concentração de risco detectada"
    else:
        alerta = "Concentração dentro do aceitável"

    classificacao = classify_risk(
        risk["volatilidade"],
        risk["maior_concentracao"]
    )

    score = portfolio_score(
        summary["roi_total"],
        classificacao["volatilidade_class"],
        classificacao["concentracao_class"]
    )

    # 🔹 4. Montar payload (ordem correta)
    data = {
        "summary": summary,
        "risk": risk,
        "classificacao": classificacao,
        "score": score,
        "ativos": df.to_dict(orient="records"),
        "alerta": alerta
    }

    # 🔹 5. IA
    analysis = generate_analysis(data)

    return {
        "data": data,
        "analysis": analysis
    }

