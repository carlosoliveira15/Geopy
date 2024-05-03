import pandas as pd

au = pd.Series([5.0, 6.1, 4.2, 2.4, 8.3], index=["A", "B", "C", "D", "E"])

ag = pd.Series({"A": 51.2, "B": 62.7, "C": 54.8, "D": 47.1, "E": 40.3})

print(au, ag)

#print(au.index)
#print(au.values)

#* Criando uma Series para o Cobre:
# Cada amostra é representada pelas letras A, B, C, D, E e seus respectivos valores

cu = pd.Series([3.2, 4.5, 2.1, 4.8, 5.4], index=["A", "B", "C", "D", "E"])

print(cu)

#* Podemos criar uma copia com a função copy()

copia_cu = cu.copy()

#* O Series possui algumas funções similares ao dicionário Python
#* Podemos adicionar e modificar valores a uma série

#copia_cu.iloc[0] = 0
#copia_cu["F"] = 10
#print(copia_cu)

index = ["A", "B", "C", "D", "E"]

zn = pd.Series(dict(zip(index, [4.0, 6.1, 3.5, 6.4, 8.9])))
pb = pd.Series(dict(zip(index, [4.6, 3.4, 9.8, 1.2, 3.3])))

print(zn[1:3])

print(pb["C":"E"])

#* Funções do pandas para localizar um termo ou buscar uma posição

print(zn.loc['B']) # loc = válido para str

print(zn.iloc[1]) # iloc = válido para int, float e a boolean