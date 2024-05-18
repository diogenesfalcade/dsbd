### Pandas

import pandas as pd

lista = [-5, 0, 8, -12, 100, 33, 7, -1, 1, 2]

serie = pd.Series(lista)

dados = {
'nome': ["Ana", "Bob", "Cleo"], 
'idade': [50, 36, 2],
'altura': [1.5, 1.73, .61]
}

df1 = pd.DataFrame(dados)

# print(df1['idade'].max())
# print(df1['idade'].min())
# print(df1['altura'].mean())
# print(df1['idade'].max())
# print(df1['altura'].min())
# print(df1['idade'].sum())


Pesos = [50.8, 75, 11.3]

df1['peso'] = Pesos

del df1['nome']

df1.pop('peso')

#df1.drop(['idade'], axis = 1, inplace=True)

df2 = pd.DataFrame([[50 ,1.50]], columns=['idade', 'altura'])

df3 = pd.concat([df1,df2], ignore_index=[True])

#df4 = pd.concat([df1,df2]).reset_index(drop = True)

print(df3)