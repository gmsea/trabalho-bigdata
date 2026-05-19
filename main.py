import pandas as pd

pd.set_option("display.max_rows", 32)

dados = pd.read_csv(
    "dados/dados_atividade.csv",
    sep=";",
    engine="python"
)

print("DATAFRAME COMPLETO:")
print(dados.to_string())

print("\nPRIMEIRAS 10 LINHAS:")
print(dados.head(10))

print("\nULTIMAS 10 LINHAS:")
print(dados.tail(10))