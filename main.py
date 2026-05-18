import pandas as pd

dados = pd.read_csv("dados/clientes.csv")

print("DATASET ORIGINAL:")
print(dados)

print("\nVALORES NULOS:")
print(dados.isnull().sum())

dados["idade"] = dados["idade"].fillna(dados["idade"].mean())

dados["salario"] = dados["salario"].fillna(dados["salario"].mean())

dados = dados.drop_duplicates()

print("\nDATASET LIMPO:")
print(dados)