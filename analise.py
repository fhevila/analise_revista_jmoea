import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter
import os

# 1. Carregar os dados limpos
df = pd.read_csv('dados_limpos.csv')  # Substitua pelo caminho correto do arquivo limpo

# 2. Criar a pasta de saída caso ela não exista
output_path = r'C:\\Users\\fhevi\\Desktop\\artigo_jmoe-main\\analise_final'
os.makedirs(output_path, exist_ok=True)

# 3. Análise de Publicações por Ano
publicacoes_por_ano = df['ano'].value_counts().sort_index()

# Plotar o gráfico e salvar
plt.figure(figsize=(10, 6))
publicacoes_por_ano.plot(kind='bar', color='skyblue')
plt.title('Número de Publicações por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Publicações')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar o gráfico
publicacoes_por_ano_plot_path = os.path.join(output_path, 'publicacoes_por_ano.png')
plt.savefig(publicacoes_por_ano_plot_path)
plt.close()

# 4. Análise de Citações (Top 10 artigos mais citados)
citacoes_por_artigo = df[['titulo', 'Citações']].sort_values(by='Citações', ascending=False)

# Salvar a tabela dos artigos mais citados em CSV
citacoes_por_artigo_path = os.path.join(output_path, 'top_10_artigos_mais_citados.csv')
citacoes_por_artigo.head(10).to_csv(citacoes_por_artigo_path, index=False)

# 5. Análise de Afiliações Institucionais
afiliacoes = df['universidade'].dropna().str.split(';').explode().value_counts()

# Plotar o gráfico de barras sobre o número de publicações por ano
plt.figure(figsize=(10, 6))
publicacoes_por_ano.plot(kind='bar', color='skyblue')
plt.title('Número de Publicações por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Publicações')
plt.xticks(rotation=45)

# Ajuste de margens
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Salvar o gráfico
publicacoes_por_ano_plot_path = os.path.join(output_path, 'publicacoes_por_ano.png')
plt.savefig(publicacoes_por_ano_plot_path)
plt.close()


# 6. Análise de Rede de Co-citação
# Contagem das co-citações (referências citadas juntas)
cocitacoes = df['referencias'].dropna().str.split(';').explode()

# Contar as co-citações (quantas vezes um artigo é citado junto com outro)
co_citacoes_count = Counter(cocitacoes)

# Criando a rede de co-citações
G = nx.Graph()

# Adicionar os nós (artigos) e as arestas (co-citações)
for artigo, count in co_citacoes_count.items():
    if count > 1:  # Filtrando co-citações que ocorrem mais de uma vez
        artigos = artigo.split(';')
        if len(artigos) > 1:
            G.add_edge(artigos[0], artigos[1], weight=count)

# Desenhar e salvar a rede de co-citações
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=5000, font_size=10, node_color='lightblue', font_weight='bold', width=1.0, edge_color='gray')
plt.title('Rede de Co-Citações')

# Salvar o gráfico
co_citacoes_plot_path = os.path.join(output_path, 'rede_co_citacoes.png')
plt.savefig(co_citacoes_plot_path)
plt.close()

# 7. Análise de Co-ocorrência de Palavras-chave
# Coletar todas as palavras-chave e contar suas ocorrências
palavras_chave = df['palavras_chave'].dropna().explode().value_counts()

# Plotar as palavras-chave mais frequentes e salvar
plt.figure(figsize=(10, 6))
palavras_chave.head(20).plot(kind='bar', color='lightgreen')
plt.title('Top 20 Palavras-chave Mais Frequentes')
plt.xlabel('Palavras-chave')
plt.ylabel('Número de Ocorrências')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar o gráfico
palavras_chave_plot_path = os.path.join(output_path, 'top_20_palavras_chave.png')
plt.savefig(palavras_chave_plot_path)
plt.close()

# 8. Salvar o DataFrame completo das palavras-chave mais frequentes
palavras_chave_path = os.path.join(output_path, 'palavras_chave_frequentes.csv')
palavras_chave.to_csv(palavras_chave_path, index=True, header=['Número de Ocorrências'])
