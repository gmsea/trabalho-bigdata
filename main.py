import pandas as pd

dados = pd.read_csv("dados/clientes.csv")

subconjunto = dados[["nome", "cidade", "salario"]]

print(subconjunto)