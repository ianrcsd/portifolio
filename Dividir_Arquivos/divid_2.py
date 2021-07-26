from os import sep
import pandas as pd
arq = r'input\db_datadesktop.csv'
numero_linhas = sum(1 for row in (open(arq, encoding="utf8")))
intervalo_arquivos = 500000
df = pd.read_csv(arq,sep=',', encoding='utf-8-sig')
cabecalho = list(df.columns)
for i in range(1,numero_linhas,intervalo_arquivos):
      df = pd.read_csv(arq,nrows = intervalo_arquivos, skiprows = i,sep=',', encoding='utf-8-sig',names=cabecalho) 
      out_csv = r'output\output' + str(i) + '.csv'
      df.to_csv(out_csv,index=False,header=True,mode='a', chunksize=intervalo_arquivos, sep=';',encoding='utf-8-sig')

