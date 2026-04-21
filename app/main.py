from app.orchestrator import run_pipeline

if __name__ == "__main__":
    result = run_pipeline("data/sample.csv")

    print("=== RESULTADO ===")
    print(result["data"])

    print("\n=== ANALISE IA ===")
    print(result["analysis"])