import pandas as pd

# Carregar os dados limpos (com o caminho correto)
df = pd.read_csv('C:\\Users\\fhevi\\Desktop\\artigo_jmoe-main\\analise_final\\dados_limpos.csv')

# 1. Remover "Index Terms\n" da primeira palavra-chave
df['palavras_chave'] = df['palavras_chave'].apply(
    lambda x: [item.replace('Index Terms\n', '').strip() for item in x.split(';')] if isinstance(x, str) else []
)

# 2. Verificando se as alterações foram feitas corretamente
print(df[['palavras_chave']].head())

# 3. Salvar os dados limpos novamente, caso precise
df.to_csv('C:\\Users\\fhevi\\Desktop\\artigo_jmoe-main\\analise_final\\dados_limpos_com_palavras_chave.csv', index=False)
