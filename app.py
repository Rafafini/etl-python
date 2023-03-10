import pandas as pd

#Variável de diretório do arquivo
contratoINSS = ('C:\\Python\\bases\\contratos-inss.csv')
contratosAdicionais = ('C:\\Python\\bases\\contratos-adicionais.csv')

#Leitura de CSV, ignorando bad lines
df = pd.read_csv(contratoINSS, encoding='latin', on_bad_lines='skip', sep=";")
df2 = pd.read_csv(contratosAdicionais, encoding = 'latin', on_bad_lines='skip', sep=";")

#Renomear Coluna
contratos = df.rename(columns={'OL Contratante' : 'Contratante'})
contratosadd = df2.rename(columns={'OL Contratante' : 'Contratante'})

#Transforma todos os dados da coluna para Maiúsculo
contratos = df['Tipo de Licitacao'].str.upper()
contratosadd = df['Tipo de Licitacao'].str.upper()

#Append de bases com a mesma estrutura
contratosnew = pd.concat([contratos, contratosadd])

print(contratosnew)

