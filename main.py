import pandas as pd

dados = pd.read_csv(
    "dados/dados_atividade.csv",
    sep=";",
    engine="python"
)

print(dados)