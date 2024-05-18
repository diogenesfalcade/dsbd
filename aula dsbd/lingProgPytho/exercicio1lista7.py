import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("informe_epidemiologico_31_03_2022_obitos_casos_municipio_0.csv", 
                 delimiter = ';',
                 usecols=['MUNICÍPIO', 'CASOS', 'ÓBITOS POR COVID-19'])

df.sort_values(by=['CASOS'], inplace = True, ascending = False)
top5 = df.head(5)
# top5.plot(kind='pie', 
#           y='CASOS', 
#           labels=top5['MUNICÍPIO'],
#           autopct='%1.1f%%')

ax = top5.plot(kind='bar', 
               x='MUNICÍPIO',
               y='CASOS')

top5.plot(kind='bar',
          x='MUNICÍPIO',
          y='ÓBITOS POR COVID-19',
          ax=ax,
          color='red')

plt.ylabel("Quantidade")
plt.xticks(rotation=45)

plt.show()