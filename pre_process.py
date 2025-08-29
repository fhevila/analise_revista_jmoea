import pandas as pd
import numpy as np

# 1. Carregar os dados CSV
df = pd.read_csv('C:\\Users\\fhevi\\Desktop\\artigo_jmoe-main\\artigos_com_citacoes.csv')

# 2. Verificar as primeiras linhas dos dados
print(df.head())

# 3. Remover espaços extras nos nomes das colunas
df.columns = df.columns.str.strip()

# 4. Converter as colunas de 'ano', 'volume' e 'numero' para inteiros
df['ano'] = pd.to_numeric(df['ano'], errors='coerce').astype(int)
df['volume'] = pd.to_numeric(df['volume'], errors='coerce').astype(int)
df['numero'] = pd.to_numeric(df['numero'], errors='coerce').astype(int)

# 5. Converter 'Citações' para numérico (tratando erros e preenchendo com 0 onde necessário)
df['Citações'] = pd.to_numeric(df['Citações'], errors='coerce').fillna(0).astype(int)

# 6. Separar 'autores' (se estiverem separados por vírgulas) em listas
df['autores'] = df['autores'].apply(lambda x: x.split(',') if isinstance(x, str) else [])

# 7. Separar 'palavras_chave' (se estiverem separados por ponto e vírgula) em listas
df['palavras_chave'] = df['palavras_chave'].apply(lambda x: x.split(';') if isinstance(x, str) else [])

# 8. Separar 'referencias' (se estiverem separados por ponto e vírgula) em listas
df['referencias'] = df['referencias'].apply(lambda x: x.split(';') if isinstance(x, str) else [])

# 9. Verificando se há valores ausentes após o pré-processamento
print(df.isnull().sum())

# 10. Salvar os dados limpos em um novo CSV
df.to_csv('dados_limpos.csv', index=False)

