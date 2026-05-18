import pandas as pd

pd.set_option("display.max_rows", 10)

dados = pd.read_csv("dados/clientes.csv")

print("PRIMEIRAS LINHAS:")
print(dados.head())

print("\nULTIMAS LINHAS:")
print(dados.tail())