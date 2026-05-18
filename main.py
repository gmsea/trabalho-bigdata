import pandas as pd

dados = pd.read_csv("dados/clientes.csv")

print("INFORMACOES DO DATASET:")
print(dados.info())

print("\nCOLUNAS:")
print(dados.columns)

print("\nDIMENSOES:")
print(dados.shape)

print("\nESTATISTICAS:")
print(dados.describe())