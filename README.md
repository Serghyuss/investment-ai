# 📊 Copiloto Financeiro com IA Local

Sistema de análise de investimentos com Inteligência Artificial Local, focado em avaliação estruturada de **rentabilidade, risco e liquidez**, com geração automática de insights.

---

## 🚀 Objetivo

Desenvolver um sistema de apoio à decisão financeira que:

- Analisa carteiras a partir de arquivos CSV (ex: Itaú)
- Calcula métricas financeiras determinísticas
- Utiliza IA local para interpretação dos dados
- Gera insights e alertas automatizados
- Opera 100% offline (privacidade total)

---

## 🧠 Arquitetura


### 🔹 Componentes:

- **Ingestão de Dados:** leitura e padronização de CSV  
- **Engine Financeira:** cálculo de ROI, risco e concentração  
- **Classificação Determinística:** regras de risco (Python)  
- **LLM Local:** interpretação com modelo LLaMA via Ollama  
- **Dashboard:** interface interativa com Streamlit  

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11+
- Pandas / NumPy
- Streamlit
- Plotly
- Ollama (IA local)
- Modelo: LLaMA 3.1 8B (quantizado)

---

## 🔐 Privacidade

Este sistema opera integralmente em ambiente local.

- Nenhum dado é enviado para APIs externas
- Processamento 100% offline
- Ideal para dados financeiros sensíveis

---

## 📊 Funcionalidades

- 📈 Cálculo de ROI por ativo e carteira
- ⚠️ Avaliação de risco (volatilidade e concentração)
- 🧠 Score da carteira (0–100)
- 🚨 Alertas automáticos
- 🤖 Análise interpretativa com IA
- 📊 Dashboard interativo

---

## 🖥️ Como executar

### 1. Clonar o projeto
```bash
git clone https://github.com/seu-usuario/investment-ai.git
cd investment-ai

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

ollama pull llama3.1:8b

streamlit run app/dashboard.py

investment-ai/
│
├── app/
│   ├── main.py
│   ├── orchestrator.py
│   ├── dashboard.py
│
├── modules/
│   ├── ingestion/
│   ├── analytics/
│   ├── llm/
│
├── utils/
│
├── data/
│
├── README.md
└── requirements.txt

🧠 Diferencial do Projeto

Este projeto aplica um conceito fundamental de engenharia de dados e IA:

Separação entre lógica determinística e interpretação cognitiva

Cálculos financeiros → feitos em Python (precisão)
Análise → feita pela IA (contexto e explicação)

<img width="1869" height="862" alt="Captura de tela 2026-04-21 171030" src="https://github.com/user-attachments/assets/80f7162e-e701-4063-adc3-51c7ea882453" />
