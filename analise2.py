import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Carregar o arquivo CSV (ajuste o caminho do arquivo conforme necessário)
data = pd.read_csv('C:\\Users\\fhevi\\Desktop\\artigo_jmoe-main\\analise_final\\arquivo_colunas_ingles.csv')

# Função para processar e contar palavras-chave, autores e afiliações
def process_keywords_and_authors(data):
    # 1. Palavras-chave dos autores (separadas por vírgula)
    keywords_authors = data['pre_keywords'].dropna().apply(lambda x: [keyword.strip() for keyword in x.split(',')])
    flat_keywords_authors = [keyword for sublist in keywords_authors for keyword in sublist]
    keywords_authors_count = Counter(flat_keywords_authors)
    
    # 2. Contagem de autores (separados por vírgula)
    authors = data['authors'].dropna().apply(lambda x: [author.strip() for author in x.split(',')])
    flat_authors = [author for sublist in authors for author in sublist]
    author_counts = Counter(flat_authors)

    # 3. Afiliações (separadas por ponto e vírgula)
    affiliations = data['university'].dropna().apply(lambda x: [affiliation.strip() for affiliation in x.split(';')])
    flat_affiliations = [affiliation for sublist in affiliations for affiliation in sublist]
    affiliation_counts = Counter(flat_affiliations)

    return keywords_authors_count, author_counts, affiliation_counts

# Função para gerar gráficos
def generate_plots(keywords_authors_count, author_counts, affiliation_counts):
    # Top 10 Palavras-chave dos Autores
    top_keywords_authors = keywords_authors_count.most_common(10)
    top_keywords_authors_df = pd.DataFrame(top_keywords_authors, columns=["Keyword", "Frequency"])
    plt.figure(figsize=(10, 6))
    top_keywords_authors_df.sort_values('Frequency', ascending=True).plot(kind='barh', x='Keyword', y='Frequency', color='lightseagreen', legend=False)
    plt.title("Top 10 Keywords of Authors", fontsize=14)
    plt.xlabel('Frequency')
    plt.ylabel('Keywords')
    plt.tight_layout()
    plt.savefig('top_10_keywords_authors.png')
    plt.show()

    # Top 10 Autores
    top_authors = author_counts.most_common(10)
    top_authors_df = pd.DataFrame(top_authors, columns=["Author", "Publications"])
    plt.figure(figsize=(10, 6))
    top_authors_df.sort_values('Publications', ascending=True).plot(kind='barh', x='Author', y='Publications', color='lightblue', legend=False)
    plt.title("Top 10 Authors by Publications", fontsize=14)
    plt.xlabel('Number of Publications')
    plt.ylabel('Authors')
    plt.tight_layout()
    plt.savefig('top_10_authors.png')
    plt.show()

    # Top 10 Afiliações
    top_affiliations = affiliation_counts.most_common(10)
    top_affiliations_df = pd.DataFrame(top_affiliations, columns=["Affiliation", "Publications"])
    plt.figure(figsize=(12, 6))
    top_affiliations_df.sort_values('Publications', ascending=True).plot(kind='barh', x='Affiliation', y='Publications', color='salmon', legend=False)
    plt.title("Top 10 Affiliations", fontsize=14)
    plt.xlabel('Number of Publications')
    plt.ylabel('Affiliations')
    plt.tight_layout()
    plt.savefig('top_10_affiliations.png')
    plt.show()

# Processar dados
keywords_authors_count, author_counts, affiliation_counts = process_keywords_and_authors(data)

# Gerar gráficos
generate_plots(keywords_authors_count, author_counts, affiliation_counts)

# Se quiser exportar os dados para importar no VOSviewer ou Cytoscape:
# Exportar para CSV para análise posterior no VOSviewer ou Cytoscape
keywords_authors_df = pd.DataFrame(keywords_authors_count.items(), columns=["Keyword", "Frequency"])
keywords_authors_df.to_csv('keywords_authors.csv', index=False)

author_counts_df = pd.DataFrame(author_counts.items(), columns=["Author", "Publications"])
author_counts_df.to_csv('author_counts.csv', index=False)

affiliation_counts_df = pd.DataFrame(affiliation_counts.items(), columns=["Affiliation", "Publications"])
affiliation_counts_df.to_csv('affiliation_counts.csv', index=False)

