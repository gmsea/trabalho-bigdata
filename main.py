import pandas as pd

dados = pd.read_csv(
    "dados/dados_atividade.csv",
    sep=";",
    engine="python"
)

subconjunto = dados[["Duration", "Pulse", "Calories"]]

print(subconjunto)