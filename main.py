import pandas as pd

dados = pd.read_csv(
    "dados/dados_atividade.csv",
    sep=";",
    engine="python"
)

copia_dados = dados.copy()

copia_dados["Date"] = copia_dados["Date"].replace(
    20201226,
    "2020/12/26"
)

copia_dados["Date"] = pd.to_datetime(
    copia_dados["Date"],
    errors="coerce"
)

print(copia_dados)