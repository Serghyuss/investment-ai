import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_analysis(data: dict):

    prompt = f"""
        Você é um analista financeiro sênior.

        Regras:
        - NÃO recalcular nada
        - NÃO reinterpretar classificações
        - Use exatamente as classificações fornecidas
        - Seja objetivo e técnico

        Dados:
        {data}

        Responda:

        1. RENTABILIDADE
        - Interprete o ROI

        2. RISCO
        - Explique a volatilidade (classificação já definida)
        - Explique a concentração (classificação já definida)

        3. PONTOS CRÍTICOS
        - Liste riscos com base nos dados

        4. AVALIAÇÃO FINAL
        - Consolide o cenário com base nas classificações fornecidas
        
        5. RESUMO EXECUTIVO (máximo 2 linhas)
        - Avaliação direta da carteira
        - Indicar se o risco está adequado ao retorno
        """
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.1:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]