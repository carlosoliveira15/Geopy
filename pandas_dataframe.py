import pandas as pd

#* Um Dataframe (df) agrupa um conjunto de Series para gerar uma tabela com colunas e linhas. 
#* Utilizando as Series criadas para fazer um Dataframe:

index = ["A", "B", "C", "D", "E"]

zn = pd.Series(dict(zip(index, [4.0, 6.1, 3.5, 6.4, 8.9])))
pb = pd.Series(dict(zip(index, [4.6, 3.4, 9.8, 1.2, 3.3])))
cu = pd.Series(dict(zip(index, [3.2, 4.5, 2.1, 4.8, 5.4])))
ag = pd.Series(dict(zip(index, [51.2, 62.7, 54.8, 47.1, 40.3])))
au = pd.Series(dict(zip(index, [5.0, 6.1, 4.2, 2.4, 8.3])))

df = pd.DataFrame({'Au':au,
                   'Ag':ag,
                   'Cu':cu,
                   'Pb':pb,
                   'Zn':zn
                   })

#* df.head() define a quantidade de Linhas que aparecerá em uma ordem de A até E conforme o exemplo:
print(df.head(2))

#* df.tail() mesma interação do head, porém na ordem de baixo para cima (E até A):

print(df.tail(2))

#* Também podemos copiar um Dataframe, armazenar em uma varíavel, mesmas funções:
# df.copy()

#* Índices e Colunas

#* Renomear colunas e índices:
df.rename(columns={"Au": "Ouro"},
          index={"A": "AM1"})

#* Em alguns casos, é necessário remover o índice para realizar operações:
df.reset_index()

#* Para descartar o índice antigo, adicionamos o parâmetro drop = True
df.reset_index(drop=True)

#* Para ser uma mudança permanente, adicionamos:
df.reset_index(drop = True, inplace = True)

#* Mudando os índices das amostras:
df.index = ["AM1", "AM2", "AM3", "AM4", "AM5"]

#* Adicionando um nome no índice:
df.index.name = 'Amostras'
#print(df)

print(df.columns) # Função para ver todas as colunas de um Dataframe
print(df.dtypes) # Função importante para saber o tipo de dados de cada coluna

#* Para ordenar uma coluna em ordem crescente ou decrescente, usar:

print(df.sort_values(by=["Au"], ascending=True)) 
# ascending = True = crescente
# ascending = False = decrescente

#* Seleção de Colunas e Linhas 