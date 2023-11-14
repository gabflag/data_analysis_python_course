# Analise grafica da selic no ano de 2023 até agosto

import pandas as pd
import matplotlib.pyplot as plt

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
df_selic.drop_duplicates(keep='last', inplace=True)
df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
data1 = pd.to_datetime('2023-01-01')
data2 = pd.to_datetime('2023-09-30')

filtro_2023 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)
df_2023 = df_selic.loc[filtro_2023]
df_2023.reset_index(drop=True, inplace=True)
print(df_2023.info())

#df_2023.plot(x='valor', y='data')
df_2023.plot(x='data', y='valor')
plt.show()
print(df_2023)
