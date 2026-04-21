import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from orchestrator import run_pipeline
from utils.helpers import format_currency, format_percent
from modules.market.market_client import get_stock_data

st.set_page_config(page_title="Investment AI", layout="wide")

st.markdown("""
<h1 style='text-align: center;'>📊 Copiloto Financeiro com IA Local</h1>
<p style='text-align: center; color: gray;'>Análise de Investimentos com Inteligência Artificial</p>
""", unsafe_allow_html=True)

st.divider()

st.subheader("🔎 Consultar Ativo")

ticker_input = st.text_input(
    "Digite o código do ativo (ex: PETR4)",
    key="ticker_input"
)

if ticker_input:
    try:
        with st.spinner("Buscando dados do ativo..."):
            stock_data = get_stock_data(ticker_input)

        st.markdown(f"### {stock_data.get('nome')} ({stock_data.get('ticker')})")

        col1, col2 = st.columns(2)

        preco = stock_data.get("preco_atual") or 0
        variacao = stock_data.get("variacao")

        col1.metric("Preço Atual", format_currency(preco))

        if variacao is not None:
            col2.metric("Variação", f"{variacao:.2f}%")
        else:
            col2.metric("Variação", "N/A")

        hist = stock_data["historico"].reset_index()

        fig = px.line(hist, x="Date", y="Close", title="Histórico de Preço")
        st.plotly_chart(fig, width="stretch")

    except Exception as e:
        st.error("Erro ao buscar o ativo. Verifique o código.")

# 🔹 Upload
uploaded_file = st.file_uploader("Envie seu CSV", type=["csv"])

if uploaded_file:

    # Salvar temporariamente
    df = pd.read_csv(uploaded_file)
    df.to_csv("data/temp.csv", index=False)

    result = run_pipeline("data/temp.csv")

    data = result["data"]
    analysis = result["analysis"]

    # 🔹 KPIs
    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Aplicado", format_currency(data['summary']['total_aplicado']))
    col2.metric("📈 Total Atual", format_currency(data['summary']['total_atual']))
    col3.metric("📊 ROI", format_percent(data['summary']['roi_total']))

    st.divider()

    # 🔹 Score
    st.subheader("🧠 Score da Carteira")
    score = data["score"]

    if score >= 80:
        color = "green"
    elif score >= 60:
        color = "orange"
    else:
        color = "red"

    st.markdown(f"""
    <h2 style='color:{color}'>Score: {score}/100</h2>
    """, unsafe_allow_html=True)

    st.progress(score / 100)

    st.divider()

    # 🔹 Gráfico de alocação
    st.subheader("📊 Distribuição da Carteira")

    df_plot = pd.DataFrame(data["ativos"])

    df_plot["valor_formatado"] = df_plot["valor_atual"].apply(format_currency)

    fig = px.pie(
        df_plot,
        names="ativo",
        values="valor_atual",
        title="Alocação por Ativo"
    )

    st.plotly_chart(fig, width="stretch")

    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.divider()

    # 🔹 Risco
    st.subheader("⚠️ Risco")

    vol = data['classificacao']['volatilidade_class']
    conc = data['classificacao']['concentracao_class']

    def risk_color(level):
        return {
            "ALTA": "red",
            "MODERADA": "orange",
            "BAIXA": "green"
        }.get(level, "gray")

    st.markdown(f"""
    **Volatilidade:** <span style='color:{risk_color(vol)}'>{format_percent(data['risk']['volatilidade'])} ({vol})</span>  
    **Concentração:** <span style='color:{risk_color(conc)}'>{format_percent(data['risk']['maior_concentracao'])} ({conc})</span>
    """, unsafe_allow_html=True)

    if "Alta" in data["alerta"]:
        st.error(f"🚨 {data['alerta']}")
    else:
        st.success(f"✅ {data['alerta']}")
    
    st.divider()

    # 🔹 Alertas
    st.subheader("🚨 Alertas")
    st.warning(data["alerta"])

    st.divider()

    # 🔹 Análise IA
    st.subheader("🤖 Análise da IA")

    analysis_html = analysis.replace("\n", "<br>")

    st.markdown(f"""
    <div style="
        background-color:#111;
        padding:20px;
        border-radius:10px;
        color:white;
        font-size:14px;
    ">
    {analysis_html}
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <p style='text-align: center; color: gray; font-size: 12px;'>
    🔒 Plataforma executada 100% em ambiente local, assegurando que todos os dados financeiros sejam processados com total privacidade, sem exposição a serviços externos.
    </p>
    """, unsafe_allow_html=True)

