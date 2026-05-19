import pandas as pd

dados = pd.read_csv(
    "dados/dados_atividade.csv",
    sep=";",
    engine="python"
)

copia_dados = dados.copy()

copia_dados["Calories"] = copia_dados["Calories"].fillna(0)

copia_dados["Date"] = copia_dados["Date"].fillna("1900/01/01")

print("ANTES DA CONVERSAO:")
print(copia_dados.to_string())

copia_dados["Date"] = copia_dados["Date"].replace(
    "1900/01/01",
    pd.NA
)

copia_dados["Date"] = copia_dados["Date"].replace(
    "20201226",
    pd.to_datetime("2020/12/26")
)

copia_dados["Date"] = pd.to_datetime(
    copia_dados["Date"]
)

copia_dados = copia_dados.dropna()

print("\nDEPOIS DA CONVERSAO:")
print(copia_dados.to_string())