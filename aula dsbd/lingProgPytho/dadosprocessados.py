import pandas as pd

import sys

import datetime as dt

arquivo = pd.read_csv('processados.csv',
        names = ['data',
        'atendimentos'])

arquivo['data'] = pd.to_datetime(arquivo['data'])

#print(arquivo.groupby('data').count())
#print(arquivo.groupby('data').sum())
#print(arquivo)
#print(type(arquivo['data'][0]))

dadosAntes = arquivo['data'][arquivo['data'] < dt.datetime(2020, 1, 1)]
dadosiguais = arquivo['data'][arquivo['data'] == dt.datetime(2018, 1,8)]
dadosAgrupados = arquivo.groupby(arquivo['data'].dt.to_period('Y'))['atendimentos'].sum()


print(dadosAntes)
print('\n')
print(dadosiguais)
print('\n')
print(dadosAgrupados)